import pandas as pd  

JKOdf = pd.read_excel("./testData/fileFromJKO.xlsx")

#Dictionary that stores unique IDS to another dictionary with important information about that person
ids = dict()

grouped = JKOdf.groupby('EDIPI')

for idCols in grouped:
    edipi = idCols[0]
    group_cols = idCols[1]

    ids[edipi] = dict()

    ids[edipi]["Name"] = group_cols["First Name"].iloc[0] + " " + group_cols["Last Name"].iloc[0]
    ids[edipi]["Category"] = group_cols["Category"].iloc[0]
    ids[edipi]["Course Names"] = list(group_cols["Course Name"])
    ids[edipi]["Completed Dt"] = list(group_cols["Completed Dt"])

def pretty_print(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty_print(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

pretty_print(ids)