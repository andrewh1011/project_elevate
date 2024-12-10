compOnTime = plugin.getCustomCol("compOnTime")
compLate = plugin.getCustomCol("compLate")
incompNYD = plugin.getCustomCol("incompNYD")
overdue = plugin.getCustomCol("overdue")
compPerc = plugin.getCustomCol("compPerc")

try:
	onTimeNum = int(compOnTime)
	lateNum = int(compLate)
	incompNYDNum = int(incompNYD)
	overdueNum = int(overdue)
	percStr = str(compPerc)
	haveAllVars = True

except:
	haveAllVars = False

if haveAllVars:
	totalAssigned = onTimeNum + lateNum + incompNYDNum + overdueNum
	numComplete = onTimeNum + lateNum

	if numComplete > overdueNum:
		if numComplete > incompNYDNum:
			plugin.setOutputAsSuccess()
		else:
			plugin.setOutputAsPending()
	else:
		if overdueNum > incompNYDNum:
			plugin.setOutputAsFailure()
		else:
			plugin.setOutputAsPending() 

	plugin.setOutputText(percStr)
	plugin.setHiddenText("") 
		
else:
	plugin.setOutputText("")			
	plugin.setOutputAsNotApplicable()
	plugin.setHiddenText("")

plugin.finalizeOutput()