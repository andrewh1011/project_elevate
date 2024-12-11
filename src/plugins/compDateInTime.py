compDate = plugin.getCustomColCell("compDate")

if plugin.isCellEmpty(compDate):
	plugin.setOutputText("")
	plugin.setOutputAsPending()
	plugin.setHiddenText("")
else:
	try:
		compDate = plugin.treatCellAsDate(compDate)
		today = datetime.today()

		if today.year > compDate.year:
			plugin.setOutputAsFailure()
		else:
			plugin.setOutputAsSuccess()

		plugin.setOutputText(compDate)
		plugin.setHiddenText("")
	except:
		plugin.setOutputText("")
		plugin.setOutputAsError()
		plugin.setHiddenText("")
	
plugin.finalizeOutput()