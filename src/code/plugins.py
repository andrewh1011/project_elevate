import inspect

#custom cols will be a dict that maps colname to index
def transformPlugin(pluginStr, customCols, rowIndex):
	for col in customCols.keys():
		colIndex = customCols[col]
		pluginStr = pluginStr.replace(col, "row.iloc[int(customCols['" + col + "'])]")
	return pluginStr	


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
	exec(pluginStr,frame.f_globals, frame.f_locals)


		