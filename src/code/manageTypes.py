import pandas as pd
from enum import Enum
import os

baseDir = os.path.dirname(__file__)
typeFilePath = os.path.join(baseDir, "../appStorage/types.csv")

#if they dont use a column that requires a number, use this.
#this prevents a number column being used from being changed to empty string which causes an error.
notUsedStr = "notUsed"

#below enum values are ids of fields from Pyqt5 form for the type input.
#each fields corresponding text label will be the fieldid + "Label".

class TypeFileColumns(Enum):
	typeName = "tName"
	colList = "colList"
	failureCond = "failureCond"
	failureInfo = "failureInfo"
	notAssignedCond = "notAssignedCond"
	notAssignedInfo = "notAssignedInfo"
	pendingCond = "pendingCond"
	pendingInfo = "pendingInfo"
	successCond = "successCond"
	successInfo = "successInfo"
	
class RequiredTypeFileColumns(Enum):
	typeName = "tName"
	colList = "colList"

#sourceFieldDict is a dict that maps source field names of the form to their filled values
def addTypeToFile(typeFieldDict):

	#if file doesnt exist yet, make sure its created
	#if it already exists, this does nothing
	f = open(typeFilePath, "a+")
	f.close() 

	df = pd.DataFrame()
	typeName = ""
	if TypeFileColumns.typeName.value in typeFieldDict.keys():
		typeName = typeFieldDict[TypeFileColumns.typeName.value]
	else:
		return False	

	try:
		df = pd.read_csv(typeFilePath, index_col = 0)
	except pd.errors.EmptyDataError:
		df = pd.DataFrame()

	if not df.empty:
		#if typeName is already there, this is basically edit functionality.
		df.loc[typeName] = list(typeFieldDict.values())
		df.to_csv(typeFilePath)
	else:
		dfNew = pd.DataFrame([typeFieldDict])
		dfNew.index = [typeName]
		dfNew.to_csv(typeFilePath)

	return True
	

def deleteTypeFromFile(name):
	#if file doesnt exist yet, make sure its created
	#if it already exists, this does nothing
	f = open(typeFilePath, "a+")
	f.close() 
	df = pd.read_csv(typeFilePath, index_col = 0)

	if not df.empty:
		if name in df.index.values.tolist():
			df.drop(name, inplace =True)
			df.to_csv(typeFilePath)
		else:
			return False
	else:
		return False

	return True

def buildTypeDataFromFile():
	#if file doesnt exist yet, make sure its created
	#if it already exists, this does nothing
	f = open(typeFilePath, "a+")
	f.close() 

	try:
		df = pd.read_csv(typeFilePath, index_col = 0)
		return df
	except pd.errors.EmptyDataError:
		return pd.DataFrame()