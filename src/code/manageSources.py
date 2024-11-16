import pandas as pd
from enum import Enum

sourceFileName = "../appStorage/sources.csv"

#if they dont use a column that requires a number, use this.
#this prevents a number column being used from being changed to empty string which causes an error.
notUsedNumber = -1

#make sure these enum values of column names match the form input field names.
class SourceFileColumns(Enum):
	sourceName = "sourceName"
	firstName = "firstName"
	lastName = "lastName"
	dueDate = "dueDate"
	compDate = "compDate"
	dodid = "dodid"
	email = "email"
	courseName = "courseName"
	
#These are the columns in the source form which should not be left blank
class RequiredSourceFileColumns(Enum):
	name = "sourceName"
	firstName = "firstName"
	dueDate = "dueDate"
	compDate = "compDate"
	courseName = "courseName"
		
#sourceFieldDict is a dict that maps source field names of the form to their filled values
def addSourceToFile(sourceFieldDict):

	df = pd.DataFrame()
	sourceName = ""
	if SourceFileColumns.sourceName.value in sourceFieldDict.keys():
		sourceName = sourceFieldDict[SourceFileColumns.sourceName.value]
	else:
		return False	

	try:
		df = pd.read_csv(sourceFileName, index_col = 0)
	except pd.errors.EmptyDataError:
		df = pd.DataFrame()

	if not df.empty:
		#if sourceName is already there, this is basically edit functionality.
		df.loc[sourceName] = sourceFieldDict.values()
		df.to_csv(sourceFileName)
	else:
		dfNew = pd.DataFrame([sourceFieldDict])
		dfNew.index = [sourceName]
		dfNew.to_csv(sourceFileName)

	return True
	

def deleteSourceFromFile(name):
	df = pd.read_csv(sourceFileName, index_col = 0)

	if not df.empty:
		if name in df.index.values.tolist():
			df.drop(name, inplace =True)
			df.to_csv(sourceFileName)
		else:
			return False
	else:
		return False

	return True

def buildSourceDataFromFile():
	#if file doesnt exist yet, make sure its created
	#if it already exists, this does nothing
	f = open(sourceFileName, "a+")
	f.close() 

	try:
		df = pd.read_csv(sourceFileName, index_col = 0)
		return df
	except pd.errors.EmptyDataError:
		return pd.DataFrame()