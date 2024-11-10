import pandas as pd

from datetime import datetime
from manageSources import *
from thefuzz import fuzz

class DateStatus(Enum):
	overdue = "IND_OVERDUE" #this person has been assigned the course, and they either completed it(after the due date) or havent completed it and its past the due date.
	ontime = "IND_ONTIME" #this person has been assigned the course, and they completed it before the due date.
	assigned = "IND_ASSIGNED" #this person has been assigned the course, and they have not completed it but it is still before the due date.
	notAssigned = "IND_NOTASSIGNED"

#for all the columns needed in the report/log building that arent already in the source storage file.
class ReportExtraColumns(Enum):
	cleanName = "cleanName"
	fullName = "fullName"
	logType = "logType"
	desc = "description"
	rowData = "rowData"

class LogTypes(Enum):
	error = "ERROR"
	action = "action"

nameMatchThreshold = 78
reportFileName = "output.xlsx"
logFileName = "log.csv"

def cleanEmail(email):
	return email.replace(" ", "").lower()
def cleanName(name):
	return name.replace(" ", "").replace("-", "").lower()
def buildCourseName(courseName, sourceName):
	return courseName + "-" + sourceName

def chooseDateIndicator(dueDate,compDate):
	if pd.isna(dueDate):
		return DateStatus.notAssigned.value

	today = datetime.today()
	if pd.isna(compDate):
		if today > dueDate:
			return DateStatus.overdue.value
		else:
			return DateStatus.assigned.value
	else:
		if compDate > dueDate:
			return DateStatus.overdue.value
		else:
			return DateStatus.ontime.value

#this makes sure we only name match rows that dont have a mismatch with dodids or emails
#dont want to give a name match on two people who have two different values for an id value.
def calculateMatchRow(cleanName,matchEmail,matchId, row):
	email = row[SourceFileColumns.email.value]
	dodid = row[SourceFileColumns.dodid.value]
	otherName = row[ReportExtraColumns.cleanName.value]

	if (email == "" or email != matchEmail) and (dodid == -1 or dodid != matchId):
		return fuzz.partial_ratio(cleanName,otherName)
	else:
		return -1	

def formatOutput(data):

	lastInfoColumnIndex = 4
	writer = pd.ExcelWriter(reportFileName)
	data.to_excel(writer, index = False, sheet_name = "Report", engine='xlsxwriter')
	rowCount = len(data.index.values.tolist())
	colCount = len(data.columns.tolist())

	book  = writer.book
	sheet = writer.sheets['Report']

	overDueColor = book.add_format({'bg_color':'#FF0000'})
	onTimeColor = book.add_format({'bg_color':'#00FF00'})
	notAssignedColor = book.add_format({'bg_color':'#C0C0C0'})
	assignedColor = book.add_format({'bg_color':'#FFFF00'})
	infoColor = book.add_format({'bg_color':'#0066CC'})
	borderColor = book.add_format({'bg_color':'#000000'})
	
	sheet.set_column(0,lastInfoColumnIndex - 1,15)
	sheet.set_column(lastInfoColumnIndex,colCount,30)
	sheet.conditional_format(1,lastInfoColumnIndex,rowCount,colCount-1,{'type':'formula','criteria': "=ISNUMBER(SEARCH(\"{0}\", _xlfn.FORMULATEXT(E2)))".format(DateStatus.overdue.value),'format': overDueColor})
	sheet.conditional_format(1,lastInfoColumnIndex,rowCount,colCount-1,{'type':'formula','criteria':"=ISNUMBER(SEARCH(\"{0}\", _xlfn.FORMULATEXT(E2)))".format(DateStatus.ontime.value),'format': onTimeColor})
	sheet.conditional_format(1,lastInfoColumnIndex,rowCount,colCount-1,{'type':'formula','criteria':"=ISNUMBER(SEARCH(\"{0}\", _xlfn.FORMULATEXT(E2)))".format(DateStatus.notAssigned.value),'format': notAssignedColor})
	sheet.conditional_format(1,lastInfoColumnIndex,rowCount,colCount-1,{'type':'formula','criteria':"=ISNUMBER(SEARCH(\"{0}\", _xlfn.FORMULATEXT(E2)))".format(DateStatus.assigned.value),'format': assignedColor})
	sheet.conditional_format(1,0,rowCount,lastInfoColumnIndex,{'type':'formula','criteria':"=AND(COLUMN(A2) < {0}, ROW(A2) < {1})".format(lastInfoColumnIndex + 1, rowCount + 2),'format': infoColor})
	
	writer._save()	

def writeLogRow(source, rowStr, logVal, desc):
	df = pd.DataFrame([{SourceFileColumns.sourceName.value: source, ReportExtraColumns.rowData.value: rowStr, ReportExtraColumns.logType.value: logVal, ReportExtraColumns.desc.value: desc}])
	df.to_csv(logFileName, index = False, header = False, mode = 'a')

#fileInfos is a list of pairs (filePath,sourceName)
#nameMatchCallback is a function that takes two names(the two that matched), returns true/false
def buildOutput(fileInfos, nameMatchCallBack):

	logHdr = pd.DataFrame(columns = [SourceFileColumns.sourceName.value, ReportExtraColumns.rowData.value, ReportExtraColumns.logType.value, ReportExtraColumns.desc.value])
	logHdr.to_csv(logFileName, index = False)

	#pandas dataframe that originally has columns dodid, email, name
	#when a new coursename is encounter, this course will be added as a column
	ids = pd.DataFrame(columns = [SourceFileColumns.dodid.value, SourceFileColumns.email.value, ReportExtraColumns.cleanName.value, ReportExtraColumns.fullName.value])

	sources = pd.read_csv(sourceFileName, index_col = 0)

	for fileInfo in fileInfos:
		filePath = fileInfo[0]
		sourceName = fileInfo[1]

		fileDf = pd.read_excel(filePath)
		
		source_indices = sources.loc[sourceName]

		emailIndex = source_indices.loc[SourceFileColumns.email.value]
		dodIndex = source_indices.loc[SourceFileColumns.dodid.value]
		firstNameIndex = source_indices.loc[SourceFileColumns.firstName.value]
		lastNameIndex = source_indices.loc[SourceFileColumns.lastName.value]
		courseNameIndex = source_indices.loc[SourceFileColumns.courseName.value]
		dueDateIndex = source_indices.loc[SourceFileColumns.dueDate.value]
		compDateIndex = source_indices.loc[SourceFileColumns.compDate.value]

		if emailIndex != -1:
			fileDf.iloc[:,emailIndex] = fileDf.iloc[:,emailIndex].fillna("")
		fileDf.iloc[:,firstNameIndex] = fileDf.iloc[:,firstNameIndex].fillna("")
		if lastNameIndex != -1:
			fileDf.iloc[:,lastNameIndex]= fileDf.iloc[:,lastNameIndex].fillna("")
		
		for ind, row in fileDf.iterrows():
			dodidText = ""
			dodidNum = -1
			email = ""
			fullName = ""
			clnName = ""

			
			if dodIndex != -1:
				dodidText = row.iloc[dodIndex]
			
			if emailIndex != -1:
				email = cleanEmail(row.iloc[emailIndex])
		
			fullName = row.iloc[firstNameIndex]	
			if lastNameIndex != -1:
				fullName = fullName + " " + row.iloc[lastNameIndex]
			clnName = cleanName(fullName)

			try:
				dodidNum = int(dodidText) if not (pd.isna(dodidText) or dodidText == "")  else -1
			except ValueError:
				dodidNum = -1
				writeLogRow(sourceName, str(row), LogTypes.error.value, "dodid not a number")

			matchIndex = -1
			
			if dodidNum != -1:
				dodidMatchIndices = ids.index[ids[SourceFileColumns.dodid.value] == dodidNum]
				if not dodidMatchIndices.empty:
					matchIndex = dodidMatchIndices[0]
					writeLogRow(sourceName, str(row), LogTypes.action.value, "automatically matched by id to: \n" + str(ids.iloc[matchIndex]))
					
			if email != "" and matchIndex == -1:	
				emailMatchIndices = ids.index[ids[SourceFileColumns.email.value] == email]
				if not emailMatchIndices.empty:
					matchIndex = emailMatchIndices[0]
					writeLogRow(sourceName, str(row), LogTypes.action.value, "automatically matched by email to: \n " + str(ids.iloc[matchIndex]))
			if matchIndex == -1:
				transformed = ids.apply(lambda row: calculateMatchRow(clnName,email,dodidNum, row), axis =1)
				if not transformed.empty:
					maxInd = transformed.idxmax()
					if transformed.iloc[maxInd] > nameMatchThreshold:
						proceed = nameMatchCallBack(fullName,ids.iloc[maxInd].loc[ReportExtraColumns.fullName.value])
						if proceed:
							matchIndex = maxInd
							writeLogRow(sourceName, str(row), LogTypes.action.value, "user matched by name to: \n" + str(ids.iloc[matchIndex]))
			if matchIndex != -1:
				matchRow = ids.loc[matchIndex]
				if matchRow.loc[SourceFileColumns.dodid.value] == -1 and dodidNum != -1:
					ids.loc[matchIndex,SourceFileColumns.dodid.value] = dodidNum
				if matchRow.loc[SourceFileColumns.email.value] == "" and email != "":
					ids.loc[matchIndex,SourceFileColumns.email.value] = email

			else:
				ids = ids._append({SourceFileColumns.dodid.value : dodidNum,SourceFileColumns.email.value: email, ReportExtraColumns.cleanName.value: clnName, ReportExtraColumns.fullName.value: fullName}, ignore_index=True)
				inds = ids.index.values.tolist()
				matchIndex = inds[len(inds)-1]
				ids.iloc[matchIndex, 4:] = "=CHOOSE(1,\"\",\"{0}\")".format(DateStatus.notAssigned.value)

			
			courseName = buildCourseName(row.iloc[courseNameIndex],sourceName)
			dueDate = row.iloc[dueDateIndex]
			compDate = row.iloc[compDateIndex]
			if not courseName in ids.columns.values.tolist():
				colInfo = {courseName: "=CHOOSE(1,\"\",\"{0}\")".format(DateStatus.notAssigned.value)}
				ids = ids.assign(**colInfo)
			try:
				dStr = str(compDate.date()) if not pd.isna(compDate) else ""
				ids.loc[matchIndex, courseName] = "=CHOOSE(1,\"{0}\",\"{1}\")".format(dStr, chooseDateIndicator(dueDate,compDate))
			except:
				ids.loc[matchIndex, courseName] = "=CHOOSE(1,\"\",\"{0}\")".format(DateStatus.notAssigned.value)
				writeLogRow(sourceName, str(row), LogTypes.error.value, "invalid complete date")
				
			

	formatOutput(ids)