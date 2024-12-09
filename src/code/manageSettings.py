from enum import Enum
import os
import json

baseDir = os.path.dirname(__file__)
settingsFilePath = os.path.join(baseDir, "../appStorage/settings.json")

#below enum values are ids of fields from Pyqt5 form for the source input.
#each fields corresponding text label id will be the fieldid + "Label".

class SettingsFileColumns(Enum):
	nameMatchThreshold = "nameMatchThreshold"
	autoMatchThreshold = "autoMatchThreshold"
	
class RequiredSettingsFileColumns(Enum):
	nameMatchThreshold = "nameMatchThreshold"
	autoMatchThreshold = "autoMatchThreshold"

#settingFieldDict is a dict that maps setting field names of the form to their filled values
def addSettingsToFile(settingFieldDict):
	
	#want to overwrite settings each time they change it.
	#there will only ever be one setting line so dont care about overwrite
	try:
		f = open(settingsFilePath, "w")
		jsonStr = json.dumps(settingFieldDict)
		f.write(jsonStr)
		f.close()
		return True 
	except:
		if not f.closed():
			f.close()
		return False	
	
def buildSettingsDataFromFile():
	
	try:
		f = open(settingsFilePath, "r")
		res = json.load(f)
		f.close() 
		return res
	except:
		if not f.closed():
			f.close()
		return {}