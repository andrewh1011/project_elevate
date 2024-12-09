
def executePlugin(pluginFile):
	
	pluginStr = ""
	try:
		f = open(pluginFile, "r")
		pluginStr = f.read()
		f.close() 
	except:
		if not f.closed():
			f.close()

	eval(pluginStr)
		