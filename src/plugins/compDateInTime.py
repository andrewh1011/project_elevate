try:
	cLoc = pd.to_datetime(plugin.getCustomCol("compDate"))
except:
	cLoc = np.nan

if pd.isnull(cLoc):
	plugin.setOutputText("")
	plugin.setOutputAsPending()
	plugin.setHiddenText("")
else:
	today = datetime.today()
	if today.year > cLoc.year:
		plugin.setOutputAsFailure()
	else:
		plugin.setOutputAsSuccess()

	plugin.setOutputText(str(cLoc.date()))
	plugin.setHiddenText("")
plugin.finalizeOutput()