import pandas as pd
from datetime import datetime
from manageSources import *

reportFileName = "output.xlsx"


def parseFile(filePath, sourceName):
	fileDf = pd.read_excel(filePath)	
	sources = pd.read_csv(sourceFileName, index_col = 0)
	
	if not sourceName in sources.index.values:
		return False
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
		ids[edipi]["EDIPI"] = grouped_rows.iloc[0,source_indices.loc[SourceFileColumns.dodid.value]]
		ids[edipi]["First Name"] = grouped_rows.iloc[0,source_indices.loc[SourceFileColumns.firstName.value]]

		if source_indices.loc[SourceFileColumns.lastName.value] != -1:
			ids[edipi]["Last Name"] = grouped_rows.iloc[0,source_indices.loc[SourceFileColumns.lastName.value]]
		
		course_names = list(grouped_rows["Course Name"])

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