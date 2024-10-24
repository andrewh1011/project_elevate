import pandas as pd
from datetime import datetime

JKOdf = pd.read_excel("./testData/fileFromJKO.xlsx")

sources = pd.read_csv('sources.csv')

#Name sourceName column and source_name lowercase to ignore case
sources['sourceName'] = sources['sourceName'].str.lower()
source_name = "JKO".lower()

#Find the row of this source in sources.csv
source_indeces = sources.loc[sources["sourceName"] == source_name]
if source_indeces.empty:
    raise Exception("SOURCE NOT FOUND")

#Store column indices in dictionary
indices_dict = {
    "firstName": source_indeces["firstName"][1]-1,
    "lastName": source_indeces["lastName"][1]-1,
    "dueDate": source_indeces["dueDate"][1]-1,
    "compDate": source_indeces["compDate"][1]-1,
    "dodid": source_indeces["dodid"][1]-1
}

#Dictionary with unique IDS as keys and another dictionary with important information as values
ids = dict()

#Groups rows by ID
idColName = JKOdf.columns[indices_dict["dodid"]]
group_by_id = JKOdf.groupby(idColName)

#Loops through the rows for each person
for idRows in group_by_id:
    edipi = idRows[0]
    grouped_rows = idRows[1]

    #Create a dictionary for this person with informatin about them
    ids[edipi] = dict()

    #Store ERIPI, name, and category
    ids[edipi]["EDIPI"] = grouped_rows.iloc[0,indices_dict["dodid"]]
    ids[edipi]["First Name"] = grouped_rows.iloc[0,indices_dict["firstName"]]
    ids[edipi]["Last Name"] = grouped_rows.iloc[0,indices_dict["lastName"]]
    # ids[edipi]["Category"] = grouped_rows["Category"].iloc[0]

    course_names = list(grouped_rows["Course Name"])
    course_completed_dates = list(grouped_rows.iloc[:,indices_dict["compDate"]])
    course_due_dates = list(grouped_rows.iloc[:,indices_dict["dueDate"]])

    #Loops through this person's courses
    for i in range(len(course_names)):
        #Pandas Timestamps
        course_completed_date = course_completed_dates[i]
        course_due_date = course_due_dates[i]

        #String
        course_name = course_names[i]

        #Course was not completed
        if pd.isna(course_completed_date):
            ids[edipi][course_name] = "NOT Completed"
            continue

        #Completed date is before current date (completed course)
        if course_completed_date <= course_due_date:
            ids[edipi][course_name] = "Completed"

        #Completed after due date
        else:
            ids[edipi][course_name] = "LATE (completed)"

output = pd.DataFrame(ids.values())

with pd.ExcelWriter('output.xlsx') as writer:
    output.to_excel(writer)
    