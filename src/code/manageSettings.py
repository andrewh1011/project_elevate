import pandas as pd
from enum import Enum
import os

baseDir = os.path.dirname(__file__)
settingsFilePath = os.path.join(baseDir, "../appStorage/settings.csv")


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
		dfNew = pd.DataFrame([settingFieldDict])
		dfNew.to_csv(settingsFilePath)	
		return True
	except:
		return False	
	
def buildSettingsDataFromFile():
	try:
		df = pd.read_csv(settingsFilePath, index_col = 0)
		#only care about the first(and only) setting row
		return df.iloc[0]
	except:
		return pd.DataFrame()