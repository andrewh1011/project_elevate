compOnTime = plugin.getCustomColCell("compOnTime")
compLate = plugin.getCustomColCell("compLate")
incompNYD = plugin.getCustomColCell("incompNYD")
overdue = plugin.getCustomColCell("overdue")
compPerc = plugin.getCustomColCell("compPerc")

try:
	compOnTime = plugin.treatCellAsNumber(compOnTime)
	compLate = plugin.treatCellAsNumber(compLate)
	incompNYD = plugin.treatCellAsNumber(incompNYD)
	overdue = plugin.treatCellAsNumber(overdue)
	compPerc = plugin.treatCellAsString(compPerc)
	haveAllVars = True
except:
	haveAllVars = False

if haveAllVars:
	numComplete = compOnTime + compLate
	if numComplete > overdue:
		if numComplete > incompNYD:
			plugin.setOutputAsSuccess()
		else:
			plugin.setOutputAsPending()
	else:
		if overdue > incompNYD:
			plugin.setOutputAsFailure()
		else:
			plugin.setOutputAsPending() 

	plugin.setOutputText(compPerc)
	plugin.setHiddenText("") 

else:
	plugin.setOutputText("")			
	plugin.setOutputAsError()
	plugin.setHiddenText("")

plugin.finalizeOutput()