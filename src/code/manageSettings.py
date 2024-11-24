import pandas as pd
from enum import Enum

settingsFileName = "../appStorage/settings.csv"

#make sure these enum values of column names match the form input field names.
class SettingsFileColumns(Enum):
	nameMatchThreshold = "nameMatchThreshold"
	autoMatchThreshold = "autoMatchThreshold"
	
#These are the columns in the settings form which should not be left blank
class RequiredSettingsFileColumns(Enum):
	nameMatchThreshold = "nameMatchThreshold"
	autoMatchThreshold = "autoMatchThreshold"

#settingFieldDict is a dict that maps setting field names of the form to their filled values
def addSettingsToFile(settingFieldDict):
	
	#want to overwrite settings each time they change it.
	#there will only ever be one setting line so dont care about overwrite
	try:
		dfNew = pd.DataFrame([settingFieldDict])
		dfNew.to_csv(settingsFileName)	
		return True
	except:
		return False	
	
def buildSettingsDataFromFile():
	try:
		df = pd.read_csv(settingsFileName, index_col = 0)
		#only care about the first(and only) setting row
		return df.iloc[0]
	except:
		return pd.DataFrame()