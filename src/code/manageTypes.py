from enum import Enum
import os
import json

baseDir = os.path.dirname(__file__)
typeFilePath = os.path.join(baseDir, "../appStorage/types.json")

#below enum values are ids of fields from Pyqt5 form for the type input.
#each fields corresponding text label will be the fieldid + "Label".

class TypeFileColumns(Enum):
	typeName = "tName"
	colList = "colList"
	pluginFile = "pluginFile"
	annotation = "annotation"
	
class RequiredTypeFileColumns(Enum):
	typeName = "tName"
	colList = "colList"
	pluginFile = "pluginFile"

emptyTypeName = "noType"
def buildEmptyType():
	dictL = {}
	dictL[TypeFileColumns.typeName.value] = emptyTypeName
	for col in TypeFileColumns:
		if col.value != TypeFileColumns.typeName.value:
			dictL[col.value] = ""
	return dictL

#sourceFieldDict is a dict that maps source field names of the form to their filled values
def addTypeToFile(typeFieldDict):

	res = {}
	try:
		f = open(typeFilePath, "r")
		res = json.load(f)
		f.close() 
	except:
		if not f.closed():
			f.close()
		res = {}

	typeName = ""
	if TypeFileColumns.typeName.value in typeFieldDict.keys():
		typeName = typeFieldDict[TypeFileColumns.typeName.value]
	else:
		return False	

	#user shouldnt be able to edit the emptyType, dont want them to add columns to it.
	if typeName in res.keys() and typeName == emptyTypeName:
		return

	#if its theres this overwrites, if not it adds a new entry
	res[typeName] = typeFieldDict
	try:
		f = open(typeFilePath, "w")
		jsonStr = json.dumps(res)
		f.write(jsonStr)
		f.close()
		return True 
	except:
		if not f.closed():
			f.close()
		return False	

def deleteTypeFromFile(name):

	res = {}
	try:
		f = open(typeFilePath, "r")
		res = json.load(f)
		f.close() 
	except:
		if not f.closed():
			f.close()
		res = {}

	if name in res.keys():
		res.pop(name)
	try:
		f = open(typeFilePath, "w")
		jsonStr = json.dumps(res)
		f.write(jsonStr)
		f.close()
		return True 
	except:
		if not f.closed():
			f.close()
		return False	

def buildTypeDataFromFile():

	try:
		addTypeToFile(buildEmptyType())
		f = open(typeFilePath, "r")
		res = json.load(f)
		f.close() 
		return res
	except:
		if not f.closed():
			f.close()
		return {}