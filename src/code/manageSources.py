from enum import Enum
import os
import json

baseDir = os.path.dirname(__file__)
sourceFilePath = os.path.join(baseDir, "../appStorage/sources.json")

#below enum values are ids of fields from Pyqt5 form for the source input.
#each fields corresponding text label will be the fieldid + "Label".

class SourceFileColumns(Enum):
	sourceName = "sourceName"
	firstName = "firstName"
	lastName = "lastName"
	dodid = "dodid"
	email = "email"
	courseName = "courseName"
	skipRows = "skipRows"
	
class RequiredSourceFileColumns(Enum):
	name = "sourceName"
	skipRows = "skipRows"

#these are columns that are stored for each source but not directly editable by the user
class ExtraSourceFileColumns(Enum):
	typeName = "typeName"
	typeCols = "typeCols"

#sourceFieldDict is a dict that maps source field names of the form to their filled values
def addSourceToFile(sourceFieldDict):

	res = {}
	try:
		f = open(sourceFilePath, "r")
		res = json.load(f)
		f.close() 
	except:
		if not f.closed():
			f.close()
		res = {}

	sourceName = ""
	if SourceFileColumns.sourceName.value in sourceFieldDict.keys():
		sourceName = sourceFieldDict[SourceFileColumns.sourceName.value]
	else:
		return False	

	#if its theres this overwrites, if not it adds a new entry
	res[sourceName] = sourceFieldDict
	try:
		f = open(sourceFilePath, "w")
		jsonStr = json.dumps(res)
		f.write(jsonStr)
		f.close()
		return True 
	except:
		if not f.closed():
			f.close()
		return False	
	

def deleteSourceFromFile(name):
	
	res = {}
	try:
		f = open(sourceFilePath, "r")
		res = json.load(f)
		f.close() 
	except:
		if not f.closed():
			f.close()
		res = {}

	if name in res.keys():
		res.pop(name)
	try:
		f = open(sourceFilePath, "w")
		jsonStr = json.dumps(res)
		f.write(jsonStr)
		f.close()
		return True 
	except:
		if not f.closed():
			f.close()
		return False	

def buildSourceDataFromFile():
	try:
		f = open(sourceFilePath, "r")
		res = json.load(f)
		f.close() 
		return res
	except:
		if not f.closed():
			f.close()
		return {}