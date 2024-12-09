import inspect
import parsing

#objects that are set by the parsing routine which will be available to plugin code that is executed
globalRow = None
globalCustomCols = None
globalOutput = ""

#0 is output text that is shown, 1 is classification indicator, 2 is hidden text
baseString = "\"{0}\",\"{1}\", \"{2}\""

hiddenText = ""
outputText = ""
outputClass = ""

#functions that a plugin user can call for their convenience
def getCustomCol(customCol):
	return globalRow.iloc[int(globalCustomCols[customCol])]

def setHiddenText(txt):
	global hiddenText
	hiddenText = txt
def setOutputText(txt):
	global outputText
	outputText = txt
def setOutputAsSuccess():
	global outputClass
	outputClass = parsing.DateStatus.ontime.value
def setOutputAsFailure():
	global outputClass
	outputClass = parsing.DateStatus.overdue.value
def setOutputAsPending():
	global outputClass
	outputClass = parsing.DateStatus.assigned.value
def setOutputAsNotApplicable():
	global outputClass
	outputClass = parsing.DateStatus.notAssigned.value
def finalizeOutput():
	global globalOutput
	globalOutput = baseString.format(outputText,outputClass,hiddenText)	

def readPlugin(pluginFile):
	pluginStr = ""
	f = open(pluginFile, "r")
	pluginStr = f.read()
	f.close() 
	return pluginStr

def executePlugin(pluginStr):
	frame = inspect.currentframe().f_back
	exec(pluginStr,frame.f_globals, frame.f_locals)


		