import inspect
import parsing
import pandas as pd

#objects that are set by the parsing routine which will be available to plugin code that is executed
globalRow = None
globalCustomCols = None
#objects that are set by the plugin for the parsing routine's use
globalOutput = ""

#objects the plugin needs
baseString = "\"{0}\",\"{1}\", \"{2}\""
hiddenText = ""
outputText = ""
outputClass = ""

#functions that a plugin user can call for their convenience
#the user can of course write whatever python code they want that doesnt use these methods, but it will be easier for those with less python experience to make plugins with these.
def getCustomColCell(customCol):
	return globalRow.iloc[int(globalCustomCols[customCol])]

def setHiddenText(item):
	global hiddenText
	hiddenText = str(item)

def setOutputText(item):
	global outputText
	outputText = str(item)

def setOutputAsSuccess():
	global outputClass
	outputClass = parsing.CellStatus.success.value

def setOutputAsFailure():
	global outputClass
	outputClass = parsing.CellStatus.failure.value

def setOutputAsPending():
	global outputClass
	outputClass = parsing.CellStatus.pending.value

def setOutputAsNotApplicable():
	global outputClass
	outputClass = parsing.CellStatus.notApplicable.value

def setOutputAsError():
	global outputClass
	outputClass = parsing.CellStatus.error.value

def treatCellAsDate(cell):
	return pd.to_datetime(cell).date()
def treatCellAsString(cell):
	return str(cell)
def treatCellAsNumber(cell):
	return int(cell)

def isCellEmpty(cell):
	return pd.isnull(cell)
def cellEqualsString(cell,s):
	return str(cell) == s

def finalizeOutput():
	global globalOutput
	globalOutput = baseString.format(outputText,outputClass,hiddenText)	

#functions for parsing interface
def readPlugin(pluginFile):
	pluginStr = ""
	f = open(pluginFile, "r")
	pluginStr = f.read()
	f.close() 
	return pluginStr

def executePlugin(pluginStr):
	frame = inspect.currentframe().f_back
	exec(pluginStr,frame.f_globals, frame.f_locals)


		