compDate = plugin.getCustomCol("compDate")
if pd.isnull(compDate):
	plugin.setOutputText("")
	plugin.setOutputAsFailure()
	plugin.setHiddenText("")
else:
	if str(compDate) == "N/A":
		plugin.setOutputText("NOT REQUIRED")
		plugin.setOutputAsNotApplicable()
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