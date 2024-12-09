import inspect

#objects that are set by the parsing routine which will be available to plugin code that is executed
globalRow = None
globalCustomCols = None
globalOutput = None

#0 is output text that is shown, 1 is classification indicator, 2 is hidden text
baseString = "\"{0}\",\"{1}\", \"{2} \""

#functions that a plugin user can call for their convenience
def getCustomCol(customCol):
	print(globalRow.iloc[int(globalCustomCols[customCol])])
	return globalRow.iloc[int(globalCustomCols[customCol])]

def setHiddenText(txt):


def setOutputText(txt):

def setOutputOnTime():

def setOutputLate():

def setOutputPending():

def setOutputNotAssigned():




def readPlugin(pluginFile):
	pluginStr = ""
	try:
		f = open(pluginFile, "r")
		pluginStr = f.read()
		f.close() 
		
	except:
		if not f.closed():
			f.close()
	return pluginStr

def executePlugin(pluginStr):
	frame = inspect.currentframe().f_back
	#print("globs ")
	#print(frame.f_globals)
	#print("locs")
	#print(frame.f_locals)
	
	exec(pluginStr,frame.f_globals, frame.f_locals)


		