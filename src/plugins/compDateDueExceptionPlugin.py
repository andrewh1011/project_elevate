compDate = plugin.getCustomColCell("compDate")

if plugin.isCellEmpty(compDate):
	plugin.setOutputText("")
	plugin.setOutputAsFailure()
	plugin.setHiddenText("")
else:
	if plugin.cellEqualsString(compDate,"DUE"):
		plugin.setOutputText("DUE")
		plugin.setOutputAsPending()
		plugin.setHiddenText("")
	else:
		try:
			compDate = plugin.treatCellAsDate(compDate)
			plugin.setOutputText(compDate)
			plugin.setOutputAsSuccess()
			plugin.setHiddenText("")
		except:
			plugin.setOutputText("")
			plugin.setOutputAsError()
			plugin.setHiddenText("")
		
plugin.finalizeOutput()