import pandas as pd
from pandas._libs.parsers import STR_NA_VALUES
import numpy as np
from datetime import datetime
from manageSources import *
from manageSettings import *
from manageTypes import *
import plugins as plugin
from thefuzz import fuzz
import os

baseDir = os.path.dirname(__file__)
reportFilePath = os.path.join(baseDir, "../output/output.xlsx")
logFilePath = os.path.join(baseDir, "../output/log.csv")

firstTrainingDataCol = 4

class CellStatus(Enum):
	failure = "IND_FAILURE" 
	success = "IND_SUCCESS" 
	pending = "IND_PENDING" 
	notApplicable = "IND_NOTAPPLICABLE"
	error = "IND_ERROR"

#for all the columns needed in the report/log building that arent already in the source storage file.
class ReportExtraColumns(Enum):
	cleanName = "cleanName"
	fullName = "fullName"
	logType = "logType"
	desc = "description"
	rowData = "rowData"
	filePath = "filePath"

class LogTypes(Enum):
	error = "ERROR"
	action = "action"

def writeLogRow(source,filePath,rowStr, logVal, desc):
	df = pd.DataFrame([{SourceFileColumns.sourceName.value: source, ReportExtraColumns.filePath.value: filePath, ReportExtraColumns.rowData.value: rowStr, ReportExtraColumns.logType.value: logVal, ReportExtraColumns.desc.value: desc}])
	df.to_csv(logFilePath, index = False, header = False, mode = 'a')

def convertToInt(value,sourceName,fileName,columnIndex):
	try:
		return int(value) if not pd.isnull(value) else -1
	except Exception:
		writeLogRow(sourceName, fileName, str(value), LogTypes.error.value, "invalid number ignored in column " + str(columnIndex))
		return -1
def convertToStr(value,sourceName,fileName,columnIndex):
	try:
		return str(value) if not pd.isnull(value) else ""
	except Exception:
		writeLogRow(sourceName, fileName, str(value), LogTypes.error.value, "invalid string ignored in column " + str(columnIndex))
		return ""
			
def forceTypeOnColumn(data, columnIndex, typeFunc, sourceName, fileName):
	if columnIndex != -1:
		data[data.columns[columnIndex]] = data[data.columns[columnIndex]].apply(lambda value: typeFunc(value,sourceName,fileName,columnIndex))

def cleanEmail(email):
	return email.replace(" ", "").lower()
def cleanName(name):
	return name.replace(" ", "").replace("-", "").lower()
def buildCourseName(courseName, sourceName):
	return courseName + "-" + sourceName

#this makes sure we only name match rows that dont have a mismatch with dodids or emails
#dont want to give a name match on two people who have two different values for an id value.
def calculateMatchRow(cleanName,matchEmail,matchId, row):
	email = row[SourceFileColumns.email.value]
	dodid = row[SourceFileColumns.dodid.value]
	otherName = row[ReportExtraColumns.cleanName.value]

	if (email == "" or matchEmail == "") and (dodid == -1 or matchId == -1):
		return fuzz.partial_ratio(cleanName,otherName)
	else:
		return -1	

def formatOutput(data):

	lastInfoColumnIndex = firstTrainingDataCol - 1
	#upper left cell where the data section of the report starts
	firstCellDates = "D2"
	#upper left cell where the id section of the report starts
	firstCellIds = "A2"

	writer = pd.ExcelWriter(reportFilePath)
	data.to_excel(writer, index = False, sheet_name = "Report", engine='xlsxwriter')
	rowCount = len(data.index.values.tolist())
	colCount = len(data.columns.tolist())

	book  = writer.book
	sheet = writer.sheets['Report']

	failureColor = book.add_format({'bg_color':'#D82C2C'})
	successColor = book.add_format({'bg_color':'#7AD52F'})
	notApplicableColor = book.add_format({'bg_color':'#C0C0C0'})
	pendingColor = book.add_format({'bg_color':'#FFFF00'})
	infoColor = book.add_format({'bg_color':'#9999FF'})
	errorColor = book.add_format({'bg_color':'#00FFFF'})
	
	sheet.set_column(0,lastInfoColumnIndex - 1,15)
	sheet.set_column(lastInfoColumnIndex,colCount-1,30)
	sheet.conditional_format(1,lastInfoColumnIndex,rowCount,colCount,{'type':'formula','criteria': "=ISNUMBER(SEARCH(\"{0}\", _xlfn.FORMULATEXT({1})))".format(CellStatus.failure.value, firstCellDates),'format': failureColor})
	sheet.conditional_format(1,lastInfoColumnIndex,rowCount,colCount,{'type':'formula','criteria':"=ISNUMBER(SEARCH(\"{0}\", _xlfn.FORMULATEXT({1})))".format(CellStatus.success.value, firstCellDates),'format': successColor})
	sheet.conditional_format(1,lastInfoColumnIndex,rowCount,colCount,{'type':'formula','criteria':"=ISNUMBER(SEARCH(\"{0}\", _xlfn.FORMULATEXT({1})))".format(CellStatus.notApplicable.value, firstCellDates),'format': notApplicableColor})
	sheet.conditional_format(1,lastInfoColumnIndex,rowCount,colCount,{'type':'formula','criteria':"=ISNUMBER(SEARCH(\"{0}\", _xlfn.FORMULATEXT({1})))".format(CellStatus.pending.value, firstCellDates),'format': pendingColor})
	sheet.conditional_format(1,lastInfoColumnIndex,rowCount,colCount,{'type':'formula','criteria':"=ISNUMBER(SEARCH(\"{0}\", _xlfn.FORMULATEXT({1})))".format(CellStatus.error.value, firstCellDates),'format': errorColor})
	sheet.conditional_format(1,0,rowCount,lastInfoColumnIndex -1,{'type':'formula','criteria':"=AND(COLUMN({2}) < {0}, ROW({2}) < {1})".format(lastInfoColumnIndex + 1, rowCount + 2 , firstCellIds),'format': infoColor})
	
	sheet.freeze_panes(0, lastInfoColumnIndex)
	writer._save()	

#fileInfos is a list of pairs (filePath,sourceName)
#nameMatchCallback is a function that takes two names(the two that matched), returns true/false
def buildOutput(fileInfos, nameMatchCallBack):

	settings = buildSettingsDataFromFile()
	nameMatchThreshold = 75
	if SettingsFileColumns.nameMatchThreshold.value in settings.keys():
		nameMatchThreshold = int(settings[SettingsFileColumns.nameMatchThreshold.value])

	autoMatchThreshold = 75
	if SettingsFileColumns.autoMatchThreshold.value in settings.keys():
		autoMatchThreshold = int(settings[SettingsFileColumns.autoMatchThreshold.value])

	logHdr = pd.DataFrame(columns = [SourceFileColumns.sourceName.value, ReportExtraColumns.filePath.value, ReportExtraColumns.rowData.value, ReportExtraColumns.logType.value, ReportExtraColumns.desc.value])
	logHdr.to_csv(logFilePath, index = False)

	#pandas dataframe that originally has columns dodid, email, name
	#when a new coursename is encounter, this course will be added as a column
	ids = pd.DataFrame(columns = [SourceFileColumns.dodid.value, SourceFileColumns.email.value, ReportExtraColumns.cleanName.value, ReportExtraColumns.fullName.value])
	#by default, info section will always have dodid, email,cleanName, and  fullName. So first real training data col starts at 4
	firstTrainingDataCol = 4
	sources = buildSourceDataFromFile()
	types = buildTypeDataFromFile()

	for fileInfo in fileInfos:
		filePath = fileInfo[0]
		sourceName = fileInfo[1]

		source_data = sources[sourceName]
		skipRows = int(source_data[SourceFileColumns.skipRows.value])#required
		emailIndex = int(source_data[SourceFileColumns.email.value]) if source_data[SourceFileColumns.email.value] != "" else -1
		dodIndex = int(source_data[SourceFileColumns.dodid.value]) if source_data[SourceFileColumns.dodid.value] != "" else -1
		firstNameIndex = int(source_data[SourceFileColumns.firstName.value]) if source_data[SourceFileColumns.firstName.value] != "" else -1
		lastNameIndex = int(source_data[SourceFileColumns.lastName.value]) if source_data[SourceFileColumns.lastName.value] != "" else -1
		courseNameIndex = int(source_data[SourceFileColumns.courseName.value]) if source_data[SourceFileColumns.courseName.value] != "" else -1

		if firstNameIndex == -1 and dodIndex == -1 and emailIndex == -1:
			return "Must have at least one identifier column(email, id, name,...) " + filePath + " Source Assigned: " + sourceName

		accepted_na_values = STR_NA_VALUES - {'N/A'}
		fileDf = pd.read_excel(filePath, header = None, keep_default_na=False, na_values=accepted_na_values)

		if skipRows > 0:
			actualRowNum = len(fileDf.index)
			#want at least one row to process for a file
			if skipRows >= actualRowNum:
				return "Skip row number too large! File: " + filePath + " Source Assigned: " + sourceName
			else:
				del fileDf
				fileDf = pd.read_excel(filePath, header = list(range(skipRows)), keep_default_na=False, na_values=accepted_na_values)
		
		lc = len(fileDf.columns) - 1
		if emailIndex > lc or dodIndex > lc or firstNameIndex > lc or lastNameIndex > lc or courseNameIndex > lc:
			return "Column Index too large! File: " + filePath + " Source Assigned: " + sourceName

		customCols = source_data[ExtraSourceFileColumns.typeCols.value]

		for colName in customCols.keys():
			colIndex = int(customCols[colName]) # required
			if colIndex > lc:
				return "Column Index too large! File: " + filePath + " Source Assigned: " + sourceName
			if colIndex == -1:
				return "Column Index invalid! You may have forgotten to change this when adding a new column to a type this source uses. File: " + filePath + " Source Assigned: " + sourceName

		plugin.globalCustomCols = customCols

		trainingTypeName = source_data[ExtraSourceFileColumns.typeName.value]
		trainingTypeData = types[trainingTypeName]

		if emailIndex != -1:
			forceTypeOnColumn(fileDf,emailIndex, convertToStr, sourceName, filePath)
		if firstNameIndex != -1:
			forceTypeOnColumn(fileDf,firstNameIndex, convertToStr, sourceName, filePath)
		if lastNameIndex != -1:
			forceTypeOnColumn(fileDf,lastNameIndex, convertToStr, sourceName, filePath)
		if courseNameIndex != -1:
			forceTypeOnColumn(fileDf,courseNameIndex, convertToStr, sourceName, filePath)
		if dodIndex != -1:
			forceTypeOnColumn(fileDf,dodIndex, convertToInt, sourceName, filePath)

		#empty type means this is an info/personel file, which we want to treat differently.
		#info files data are solely used to add more information to person info section or course names
		if trainingTypeName != emptyTypeName:
			pluginFilePath = trainingTypeData[TypeFileColumns.pluginFile.value]
			try:
				pluginStr = plugin.readPlugin(pluginFilePath)
			except:
				return "Error reading plugin. It is possible this plugin file has moved somewhere else or it is being used by another program. File: " + filePath
		else:
			explicitColIndices = []

			for ind in [emailIndex,firstNameIndex,lastNameIndex,courseNameIndex,dodIndex]:
				if ind != -1:
					explicitColIndices.append(ind)

			fileCols = list(fileDf.columns)		
			possibleIndices = range(len(fileDf.columns))
			infoCols = {}
			for ind in possibleIndices:
				if ind not in explicitColIndices:
					infoCols[fileCols[ind]] = ind

			#list of len 2 arrays: first num is index in file being read, second is index in ids
			convertedIndices = []
			for infoCol in infoCols.keys():
				ids.insert(0, infoCol, "" , allow_duplicates=True)
				firstTrainingDataCol = firstTrainingDataCol + 1
				for convInd in convertedIndices:
					convInd[1] = convInd[1] + 1
				convertedIndices.append([infoCols[infoCol], 0])
		

		for ind, row in fileDf.iterrows():
			plugin.globalRow = row

			dodidNum = -1
			email = ""
			fullName = ""
			clnName = ""

			if dodIndex != -1:
				dodidNum = row.iloc[dodIndex]
			
			if emailIndex != -1:
				email = cleanEmail(row.iloc[emailIndex])
		
			if firstNameIndex != -1:
				fullName = row.iloc[firstNameIndex]	
			if lastNameIndex != -1:
				fullName = fullName + " " + row.iloc[lastNameIndex]
			clnName = cleanName(fullName)

			#user claims to have given at least one identifier column, yet didnt get any identifier information.
			#this is a useless row, so ignore it.
			if clnName == "" and email == "" and dodidNum == -1:
				writeLogRow(sourceName, filePath, row.to_string(), LogTypes.action.error, "blank row(" + str(ind) + ") with no identifying information ignored.")
				continue

			matchIndex = -1
			
			if dodidNum != -1:
				dodidMatchIndices = ids.index[ids[SourceFileColumns.dodid.value] == dodidNum]
				if not dodidMatchIndices.empty:
					matchIndex = dodidMatchIndices[0]
					writeLogRow(sourceName, filePath, row.to_string(), LogTypes.action.value, "automatically matched by id to: \n" + ids.iloc[matchIndex, :4].to_string())
					
			if email != "" and matchIndex == -1:	
				emailMatchIndices = ids.index[ids[SourceFileColumns.email.value] == email]
				if not emailMatchIndices.empty:
					matchIndex = emailMatchIndices[0]
					writeLogRow(sourceName, filePath, row.to_string(), LogTypes.action.value, "automatically matched by email to: \n " + ids.iloc[matchIndex, :4].to_string())
			if matchIndex == -1:
				transformed = ids.apply(lambda row: calculateMatchRow(clnName,email,dodidNum, row), axis =1)
				if not transformed.empty:
					matchIndices = transformed[transformed > nameMatchThreshold].index.to_list()
					matchIndices.sort(key=lambda ind: transformed.iloc[ind])
					for index in matchIndices:
						if transformed.iloc[index] > autoMatchThreshold:
							matchIndex = index
							writeLogRow(sourceName, filePath, row.to_string() , LogTypes.action.value, "automatically matched by name to: \n" + ids.iloc[matchIndex, :4].to_string())
							break
						else:
							results = nameMatchCallBack(fullName,ids.iloc[index].loc[ReportExtraColumns.fullName.value])
							yesAnswer = results[0]
							keepGoing = results[1]
							if keepGoing:
								if yesAnswer:
									matchIndex = index
									writeLogRow(sourceName, filePath, row.to_string() , LogTypes.action.value, "user matched by name to: \n" + ids.iloc[matchIndex, :4].to_string())
									break
							else:
								return "Parsing process stopped manually during name match."
			if matchIndex != -1:
				#fill in any new data that we gained for a person from a match
				matchRow = ids.loc[matchIndex]
				if matchRow.loc[SourceFileColumns.dodid.value] == -1 and dodidNum != -1:
					ids.loc[matchIndex,SourceFileColumns.dodid.value] = dodidNum
				if matchRow.loc[SourceFileColumns.email.value] == "" and email != "":
					ids.loc[matchIndex,SourceFileColumns.email.value] = email
				if matchRow.loc[ReportExtraColumns.fullName.value] == "" and fullName != "":
					ids.loc[matchIndex,ReportExtraColumns.fullName.value] = fullName

				if trainingTypeName == emptyTypeName:
					for convInd in convertedIndices:
						fileInd = convInd[0]
						idInd = convInd[1]
						if str(matchRow.iloc[idInd]) == "" and str(row.iloc[fileInd]) != "":
							ids.iloc[matchIndex,idInd] = str(row.iloc[fileInd])

			else:
				ids = ids._append({SourceFileColumns.dodid.value : dodidNum,SourceFileColumns.email.value: email, ReportExtraColumns.cleanName.value: clnName, ReportExtraColumns.fullName.value: fullName}, ignore_index=True)
				inds = ids.index.values.tolist()
				matchIndex = inds[len(inds)-1]
				matchRow = ids.loc[matchIndex]
				if trainingTypeName == emptyTypeName:
					for convInd in convertedIndices:
						fileInd = convInd[0]
						idInd = convInd[1]
						ids.iloc[matchIndex, idInd] = str(row.iloc[fileInd])
				ids.iloc[matchIndex, firstTrainingDataCol:] = "=CHOOSE(1,{0},{1},{2})".format("\"\"", "\"" + CellStatus.notApplicable.value + "\"", "\"\"")

			if trainingTypeName != emptyTypeName:
				if courseNameIndex != -1:
					courseName = buildCourseName(row.iloc[courseNameIndex],sourceName)
				else:
					#if no coursename, file is assumed to be describing a single training module. In this case, sourceName is the same as courseName
					courseName = sourceName

				if not courseName in ids.columns.values.tolist():
					colInfo = {courseName: "=CHOOSE(1,{0},{1},{2})".format("\"\"", "\"" + CellStatus.notApplicable.value + "\"", "\"\"")}
					ids = ids.assign(**colInfo)
			
			if trainingTypeName != emptyTypeName:
				try:
					plugin.executePlugin(pluginStr)
				except Exception as e:
					return "Error while running plugin. File: " + pluginFilePath + " Error: " + str(e)
				
				builtOutput = plugin.globalOutput
				ids.loc[matchIndex, courseName] = "=CHOOSE(1,{0})".format(builtOutput)
			
	ids.drop(ReportExtraColumns.cleanName.value, axis=1, inplace=True)
	formatOutput(ids)
	return "Output generated in output.xlsx file."