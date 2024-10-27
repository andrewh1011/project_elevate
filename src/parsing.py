import pandas as pd
from datetime import datetime
from manageSources import *
from thefuzz import fuzz

reportFileName = "output.xlsx"
personNameColumn = "cleanName"
nameMatchThreshold = 78


def cleanEmail(email):
	return email.replace(" ", "").lower()
def cleanName(name):
	return name.replace(" ", "").replace("-", "").lower()

#fileInfos is a list of pairs (filePath,sourceName)
def buildIds(fileInfos):
	#pandas dataframe that has columns dodid, email, name
	ids = pd.DataFrame(columns = [SourceFileColumns.dodid.value, SourceFileColumns.email.value, personNameColumn])
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

		if emailIndex != -1:
			fileDf.iloc[:,emailIndex].fillna("", inplace=True)
		fileDf.iloc[:,firstNameIndex].fillna("", inplace=True)
		if lastNameIndex != -1:
			fileDf.iloc[:,lastNameIndex].fillna("", inplace=True)
		
		for ind, row in fileDf.iterrows():
			print(row)
			dodidText = ""
			dodidNum = -1
			email = ""
			name = ""

			
			if dodIndex != -1:
				dodidText = row.iloc[dodIndex]
			
			if emailIndex != -1:
				email = cleanEmail(row.iloc[emailIndex])
		
			name = row.iloc[firstNameIndex]	
			if lastNameIndex != -1:
				name = name + row.iloc[lastNameIndex]
			name = cleanName(name)

			try:
				dodidNum = int(dodidText)
			except ValueError:
				dodid = -1

			matchIndex = -1

			if dodidNum != -1:
				dodidMatchIndices = ids.index[ids[SourceFileColumns.dodid.value] == dodidNum]
				if not dodidMatchIndices.empty:
					print("matched dodid")
					matchIndex = dodidMatchIndices[0]
					
			if email != "" and matchIndex == -1:	
				emailMatchIndices = ids.index[ids[SourceFileColumns.email.value] == email]
				if not emailMatchIndices.empty:
					print("matched email")
					matchIndex = emailMatchIndices[0]
			if matchIndex == -1:
				transformed = ids[personNameColumn].map(lambda otherName: fuzz.partial_ratio(otherName,name))
				if not transformed.empty:
					maxInd = transformed.idxmax()
					if transformed.iloc[maxInd] > nameMatchThreshold:
						matchIndex = maxInd
						print("matched name ")
						print(ids.iloc[maxInd])
			if matchIndex != -1:
				matchRow = ids.loc[matchIndex]
				if matchRow.loc[SourceFileColumns.dodid.value] == -1 and dodidNum != -1:
					ids.loc[matchIndex,SourceFileColumns.dodid.value] = dodidNum
				if matchRow.loc[SourceFileColumns.email.value] == "" and email != "":
					ids.loc[matchIndex,SourceFileColumns.email.value] = email

			else:
				print("new row")
				ids = pd.concat([pd.DataFrame([[dodidNum,email,name]], columns= ids.columns), ids], ignore_index=True)

	print(ids)
				
		
		
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

	#Groups rows by ID
	id_col_name = fileDf.columns[source_indices.loc[SourceFileColumns.dodid.value]]
	group_by_id = fileDf.groupby(id_col_name)

	#Loops through the rows for each person
	for idRows in group_by_id:
		edipi = idRows[0]
		grouped_rows = idRows[1]

		#Create a dictionary for this person with informatin about them
		ids[edipi] = dict()

		#Store ERIPI, name, and category
		ids[edipi][source_indices.loc[SourceFileColumns.dodid.value]] = grouped_rows.iloc[0,source_indices.loc[SourceFileColumns.dodid.value]]
		ids[edipi][source_indices.loc[SourceFileColumns.firstName.value]] = grouped_rows.iloc[0,source_indices.loc[SourceFileColumns.firstName.value]]

		if source_indices.loc[SourceFileColumns.lastName.value] != -1:
			ids[edipi][source_indices.loc[SourceFileColumns.lastName.value]] = grouped_rows.iloc[0,source_indices.loc[SourceFileColumns.lastName.value]]
		
		course_names = list(grouped_rows[SourceFileColumns.courseName.value])

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
				ids[edipi][course_name] = "NOT Completed"
				continue

			#Completed date is before current date (completed course)
			if course_completed_date <= course_due_date:
				ids[edipi][course_name] = "Completed"

			#Completed after due date
			else:
				ids[edipi][course_name] = "LATE (completed)"

	output = pd.DataFrame(ids.values())

	with pd.ExcelWriter(reportFileName) as writer:
		output.to_excel(writer)