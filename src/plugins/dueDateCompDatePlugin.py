try:
	dLoc = pd.to_datetime(plugin.getCustomCol("dueDate"))
except:
	dLoc = np.nan
try:
	cLoc = pd.to_datetime(plugin.getCustomCol("compDate"))
except:
	cLoc = np.nan

if pd.isnull(dLoc):
	if pd.isnull(cLoc):
		plugin.setOutputText("")
		plugin.setOutputAsNotApplicable()
	else:
		plugin.setOutputText(str(cLoc.date()))
		plugin.setOutputAsSuccess()
		plugin.setHiddenText("DUE:NONE")
else:
	today = datetime.today()
	if pd.isnull(cLoc):
		if today > dLoc:
			plugin.setOutputText("")
			plugin.setOutputAsFailure()
			plugin.setHiddenText("DUE:" + str(dLoc.date()))
		else:
			plugin.setOutputText("")
			plugin.setOutputAsPending()
			plugin.setHiddenText("DUE:" + str(dLoc.date()))
	else:
		if cLoc > dLoc:
			plugin.setOutputText(str(cLoc.date()))
			plugin.setOutputAsFailure()
			plugin.setHiddenText("DUE:" + str(dLoc.date()))
		else:
			plugin.setOutputText(str(cLoc.date()))
			plugin.setOutputAsSuccess()
			plugin.setHiddenText("DUE:" + str(dLoc.date()))
plugin.finalizeOutput()