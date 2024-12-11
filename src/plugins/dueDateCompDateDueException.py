dueDate = plugin.getCustomColCell("dueDate")
compDate = plugin.getCustomColCell("compDate")
today = datetime.today()

if plugin.isCellEmpty(compDate):
	if plugin.isCellEmpty(dueDate):
		plugin.setOutputText("")
		plugin.setOutputAsNotApplicable()
		plugin.setHiddenText("")
	else:
		try:
			dueDate = plugin.treatCellAsDate(dueDate)
			if today > dueDate:
				plugin.setOutputAsFailure()
			else:
				plugin.setOutputAsPending()
			plugin.setOutputText("")
			plugin.setHiddenText("DUE:" + plugin.treatCellAsString(dueDate))
		except:
			plugin.setOutputText("")
			plugin.setOutputAsError()
			plugin.setHiddenText("")
else:
	if plugin.cellEqualsString(compDate, "DUE"):
		plugin.setOutputText("DUE")
		plugin.setOutputAsPending()
		plugin.setHiddenText("")
	else:
		try:
			compDate = plugin.treatCellAsDate(compDate)	
			if plugin.isCellEmpty(dueDate):
				plugin.setOutputText(compDate)
				plugin.setOutputAsSuccess()
				plugin.setHiddenText("")
			else:
				dueDate = plugin.treatCellAsDate(dueDate)
				if compDate > dueDate:
					plugin.setOutputAsFailure()
				else:
					plugin.setOutputAsSuccess()
				plugin.setOutputText(compDate)
				plugin.setHiddenText("DUE:" + plugin.treatCellAsString(dueDate))
		except:
			plugin.setOutputText("")
			plugin.setOutputAsError()
			plugin.setHiddenText("")

plugin.finalizeOutput()