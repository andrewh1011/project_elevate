import pandas as pd

#it is expected this file will be in the current working directory.
sourceFileName = "sources.csv"
sourceName = "sourceName"
nameCol = "nameCol"
dateCol = "dateCol"
idCol = "idCol"


def addSourceToFile(name, nCol,dCol,iCol):

	df = pd.DataFrame()

	try:
		df = pd.read_csv(sourceFileName, index_col = 0)
	except pd.errors.EmptyDataError:
		df = pd.DataFrame()

	if not df.empty:
		if name in df[sourceName].to_list():
			#source already exists
			return False
		else:
			df.loc[name] = [name,nCol,dCol,iCol]
			df.to_csv(sourceFileName)
	else:
		dfNew = pd.DataFrame([{sourceName:name,nameCol: nCol, dateCol : dCol, idCol : iCol}])
		dfNew.index = [name]
		dfNew.to_csv(sourceFileName)

	return True
	

def deleteSourceFromFile(name):
	df = pd.read_csv(sourceFileName, index_col = 0)

	if not df.empty:
		if name in df.index.values.tolist():
			df.drop(name, inplace =True)
			df.to_csv(sourceFileName)
		else:
			return False
	else:
		return False

	return True

def buildSourceDataFromFile():
	#if file doesnt exist yet, make sure its created
	#if it already exists, this does nothing
	f = open(sourceFileName, "a+")
	f.close() 

	try:
		df = pd.read_csv(sourceFileName)
		return df
	except pd.errors.EmptyDataError:
		return pd.DataFrame()