import pandas as pd

from datetime import datetime
from manageSources import *
from thefuzz import fuzz

reportFileName = "output.xlsx"
cleanNameColumn = "cleanName"
fullNameColumn = "fullName"
nameMatchThreshold = 78

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
	otherName = row[cleanNameColumn]

	if (email == "" or email != matchEmail) and (dodid == -1 or dodid != matchId):
		return fuzz.partial_ratio(cleanName,otherName)
	else:
		return -1	

def formatOutput(data):

	writer = pd.ExcelWriter(reportFileName)
	data.to_excel(writer, index = False, sheet_name = "Report", engine='xlsxwriter')
	rowCount = len(data.index.values.tolist())
	colCount = len(data.columns.tolist())

	book  = writer.book
	sheet = writer.sheets['Report']
	overDueColor = book.add_format({'bg_color':'red'})
	onTimeColor = book.add_format({'bg_color':'green'})
	emptyColor = book.add_format({'bg_color':'#C0C0C0'})
	infoColor = book.add_format({'bg_color':'#0066CC'})
	borderColor = book.add_format({'bg_color':'#000000'})
	
	#sheet.conditional_format(rowCount+1,0,sheet.dim_rowmax,sheet.dim_colmax,{'type':'blanks','format':borderColor})
	sheet.set_column(0,3,15,infoColor)
	sheet.set_column(4,colCount,30)
	sheet.conditional_format(1,4,rowCount-1,colCount-1,{'type':'blanks','format':emptyColor})
	
	writer._save()	

#fileInfos is a list of pairs (filePath,sourceName)
#nameMatchCallback is a function that takes two names(the two that matched), returns true/false
def buildOutput(fileInfos, nameMatchCallBack):

	#pandas dataframe that originally has columns dodid, email, name
	#when a new coursename is encounter, this course will be added as a column
	ids = pd.DataFrame(columns = [SourceFileColumns.dodid.value, SourceFileColumns.email.value, cleanNameColumn, fullNameColumn])
	
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
				dodidNum = int(dodidText)
			except ValueError:
				dodid = -1

			matchIndex = -1
			
			if dodidNum != -1:
				dodidMatchIndices = ids.index[ids[SourceFileColumns.dodid.value] == dodidNum]
				if not dodidMatchIndices.empty:
					matchIndex = dodidMatchIndices[0]
					
			if email != "" and matchIndex == -1:	
				emailMatchIndices = ids.index[ids[SourceFileColumns.email.value] == email]
				if not emailMatchIndices.empty:
					matchIndex = emailMatchIndices[0]
			if matchIndex == -1:
				transformed = ids.apply(lambda row: calculateMatchRow(clnName,email,dodidNum, row), axis =1)
				if not transformed.empty:
					maxInd = transformed.idxmax()
					if transformed.iloc[maxInd] > nameMatchThreshold:
						proceed = nameMatchCallBack(fullName,ids.iloc[maxInd].loc[fullNameColumn])
						if proceed:
							matchIndex = maxInd
			if matchIndex != -1:
				matchRow = ids.loc[matchIndex]
				if matchRow.loc[SourceFileColumns.dodid.value] == -1 and dodidNum != -1:
					ids.loc[matchIndex,SourceFileColumns.dodid.value] = dodidNum
				if matchRow.loc[SourceFileColumns.email.value] == "" and email != "":
					ids.loc[matchIndex,SourceFileColumns.email.value] = email

			else:
				ids = ids._append({SourceFileColumns.dodid.value : dodidNum,SourceFileColumns.email.value: email, cleanNameColumn: clnName, fullNameColumn: fullName}, ignore_index=True)
				inds = ids.index.values.tolist()
				matchIndex = inds[len(inds)-1]

			
			courseName = buildCourseName(row.iloc[courseNameIndex],sourceName)
			dueDate = row.iloc[dueDateIndex]
			if not courseName in ids.columns.values.tolist():
				colInfo = {courseName: ""}
				ids = ids.assign(**colInfo)
			ids.loc[matchIndex, courseName] = dueDate

	print(ids)
	formatOutput(ids)
	
				
		
		
def parseFile(filePath, sourceName):
	fileDf = pd.read_excel(filePath)	
	sources = pd.read_csv(sourceFileName, index_col = 0)
	
	source_indices = sources.loc[sourceName]
	
	#make sure no column indices entered by user fall outside possible columns index range for this file
	largestIndexPoss = len(fileDf.columns) -1
	for sourceColumn in SourceFileColumns:
		if sourceColumn != SourceFileColumns.sourceName:
			colIndex = source_indices.loc[sourceColumn.value]
			if source_indices.loc[sourceColumn.value] != -1 and colIndex > largestIndexPoss:
				return False

	#Dictionary with unique IDS as keys and another dictionary with important information as values
	ids = dict()

	#Groups rows by ID if present, if not group by email
	if source_indices.dodid >= 0:
		identifier_col_name = fileDf.columns[source_indices.loc[SourceFileColumns.dodid.value]]
	elif source_indices.email >= 0:
		identifier_col_name = fileDf.columns[source_indices.loc[SourceFileColumns.email.value]]
	group_by = fileDf.groupby(identifier_col_name)

	#Loops through the rows for each person
	for person in group_by:
		identifier = person[0]
		grouped_rows = person[1]

		#Create a dictionary for this person with informatin about them
		ids[identifier] = dict()

		#Store ERIPI, name, and category
		ids[identifier][source_indices.loc[SourceFileColumns.dodid.value]] = grouped_rows.iloc[0,source_indices.loc[SourceFileColumns.dodid.value]]
		ids[identifier][source_indices.loc[SourceFileColumns.firstName.value]] = grouped_rows.iloc[0,source_indices.loc[SourceFileColumns.firstName.value]]

		if source_indices.loc[SourceFileColumns.lastName.value] != -1:
			ids[identifier][source_indices.loc[SourceFileColumns.lastName.value]] = grouped_rows.iloc[0,source_indices.loc[SourceFileColumns.lastName.value]]
		
		course_names = list(grouped_rows.iloc[:,source_indices.loc[SourceFileColumns.courseName.value]])

		course_completed_dates = list(grouped_rows.iloc[:,source_indices.loc[SourceFileColumns.compDate.value]])
		course_due_dates = list(grouped_rows.iloc[:,source_indices.loc[SourceFileColumns.dueDate.value]])

		#Loops through this person's courses
		for i in range(len(course_names)):
			#Pandas Timestamps
			course_completed_date = course_completed_dates[i]
			course_due_date = course_due_dates[i]
			#String
			course_name = course_names[i]

			#Course was not completed
			if pd.isna(course_completed_date):
				ids[identifier][course_name] = "NOT Completed"
				continue

			#Completed date is before current date (completed course)
			if course_completed_date <= course_due_date:
				ids[identifier][course_name] = "Completed"

			#Completed after due date
			else:
				ids[identifier][course_name] = "LATE (completed)"

	output = pd.DataFrame(ids.values())

	with pd.ExcelWriter(reportFileName) as writer:
		output.to_excel(writer)