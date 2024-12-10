compDate = plugin.getCustomCol("compDate")
if pd.isnull(compDate):
	plugin.setOutputText("")
	plugin.setOutputAsFailure()
	plugin.setHiddenText("")
else:
	if str(compDate) == "DUE":
		plugin.setOutputText("DUE")
		plugin.setOutputAsPending()
		plugin.setHiddenText("")
	else:
		try:
			cLoc = pd.to_datetime(compDate)
		except:
			cLoc = np.nan

		if pd.isnull(cLoc):
			plugin.setOutputText("")
			plugin.setOutputAsNotApplicable()
			plugin.setHiddenText("")
		else:
			plugin.setOutputText(str(cLoc.date()))
			plugin.setOutputAsSuccess()
			plugin.setHiddenText("")
plugin.finalizeOutput()