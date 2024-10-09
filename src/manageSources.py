import pandas as pd

#it is expected this file will be in the current working directory.
sourceFileName = "sources.csv"


def addSourceToFile(name, nCol,dCol,iCol):

	df = pd.DataFrame()

	try:
		df = pd.read_csv(sourceFileName)
	except pd.errors.EmptyDataError:
		df = pd.DataFrame()

	if not df.empty:
		if name in df["name"]:
			#source already exists
			return False
		else:
			df.loc[name] = [name,nCol,dCol,iCol]
			df.to_csv(sourceFileName)
	else:
		dfNew = pd.DataFrame({"name":[name],"nameCol":[nCol], "dateCol" : [dCol], "idCol" :[iCol]})
		dfNew.index = [name]
		dfNew.to_csv(sourceFileName)

	return True
	

def deleteSourceFromFile(name):
	df = pd.read_csv(sourceFileName, header = None)

	if df:
		if(df.loc[name]):
			df.drop(name, inplace =true)
			df.to_csv(sourceFileName)
		else:
			return False
	else:
		return False

	return True

def buildSourceDataFromFile():

	f = open(sourceFileName, "a+")
	f.close() 

	try:
		df = pd.read_csv(sourceFileName)
		return df
	except pd.errors.EmptyDataError:
		return pd.DataFrame()