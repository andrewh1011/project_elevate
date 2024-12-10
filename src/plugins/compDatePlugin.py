try:
	cLoc = pd.to_datetime(plugin.getCustomCol("compDate"))
except:
	cLoc = np.nan

if pd.isnull(cLoc):
	plugin.setOutputText("DUE")
	plugin.setOutputAsPending()
	plugin.setHiddenText("")
else:
	plugin.setOutputText(str(cLoc.date()))
	plugin.setOutputAsSuccess()
	plugin.setHiddenText("")
plugin.finalizeOutput()