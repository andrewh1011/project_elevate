import pandas as pd
from datetime import datetime
from manageSources import *
from thefuzz import fuzz

reportFileName = "output.xlsx"


def cleanEmail(email):
	return email.replace(" ", "").lower()
def cleanName(name):
	return name.replace(" ", "").replace("-", "").lower()

#fileInfos is a list of pairs (filePath,sourceName)
def buildIdDict(fileInfos):
	#pandas dataframe that has columns dodid, email, name
	ids = pd.DataFrame(columns = [SourceFileColumns.dodid, SourceFileColumns.email, "cleanName"])
	sources = pd.read_csv(sourceFileName, index_col = 0)

	for fileInfo in fileInfos:
		filePath = fileInfo[0]
		sourceName = fileInfo[1]

		fileDf = pd.read_excel(filePath)
		source_indices = sources.loc[sourceName]
		
		for row in fileDf.iloc[:]:
			dodidText = ""
			dodidNum = -1
			email = ""
			name = ""

			if source_indices.loc[SourceFileColumns.dodid.value] != -1:
				dodidText = row.loc[SourceFileColumns.dodid.value]
			if source_indices.loc[SourceFileColumns.email.value] != -1:
				email = cleanEmail(row.loc[SourceFileColumns.email.value])

			name = row.loc[SourceFileColumns.firstName.value]
			if source_indices.loc[SourceFileColumns.lastName.value] != -1:
				name = name + row.loc[SourceFileColumns.lastName.value]

			name = cleanName(name)

			try:
				dodidNum = int(dodidText)
			except ValueError:
				dodid = -1


			matchIndex = -1

			if dodidNum != -1:
				dodidMatchIndices = ids.index[ids[SourceFileColumns.dodid.value] == dodidNum]
				if dodidMatchIndices:
					matchIndex = dodidMatchIndices[0]
			if email != "" and matchIndex == -1:	
				emailMatchIndices = ids.index[ids[SourceFileColumns.email.value] == email]
					if emailMatchIndices:
						matchIndex = dodidMatchIndices[0]
			if matchIndex == -1:
				nameMatchIndices = ids.index[fuzz.partial_ratio(ids["cleanName"],name) > 95]
						maxIndex = -1
						maxVal = -1
						for nameMatchIndex in nameMatchIndices:
							score = fuzz.partial_ratio(ids.iloc[nameMatchIndex, "cleanName"], name)
							if score > maxVal:
								maxVal = score
								maxIndex = nameMatchIndex
						
						matchIndex = maxIndex		
				
			if matchIndex != -1:
				matchRow = ids.loc[matchRow]
				if matchRow.loc[SourceFileColumns.dodid.value] == -1 and dodidNum != -1
					ids.loc[matchRow,SourceFileColumns.dodid.value] = dodidNum
				if matchRow.loc[SourceFileColumns.email.value] == -1 and email != ""
					ids.loc[matchRow,SourceFileColumns.email.value] = email

			else:
				ids = pd.concat([pd.DataFrame([[dodidNum,email,name]], columns= ids.columns), ids], ignore_index=True)
				
		
		
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