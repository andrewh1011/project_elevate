import pandas as pd
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

class ExtraSourceFileColumns(Enum):
	typeName = "typeName"
	typeCols = "typeCols"
	
class RequiredSourceFileColumns(Enum):
	name = "sourceName"
	skipRows = "skipRows"

#sourceFieldDict is a dict that maps source field names of the form to their filled values
def addSourceToFile(sourceFieldDict):

	res = {}
	#try
	f = open(sourceFilePath, "r")
	res = json.load(f)
	f.close() 
	#except:
		#res = {}

	sourceName = ""
	if SourceFileColumns.sourceName.value in sourceFieldDict.keys():
		sourceName = sourceFieldDict[SourceFileColumns.sourceName.value]
	else:
		return False	

	#if its theres this overwrites, if not it adds a new entry
	res[sourceName] = sourceFieldDict
	#try:
	f = open(sourceFilePath, "w")
	jsonStr = json.dumps(res)
	f.write(jsonStr)
	f.close()
	return True 
	#except:
	#	return False	
	

def deleteSourceFromFile(name):
	
	res = {}
	try:
		f = open(sourceFilePath, "r")
		res = json.load(f)
		f.close() 
	except:
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
		return False	

def buildSourceDataFromFile():
	try:
		f = open(sourceFilePath, "r")
		res = json.load(f)
		f.close() 
		return res
	except:
		return {}