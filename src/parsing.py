import pandas as pd
from datetime import datetime

JKOdf = pd.read_excel("./testData/fileFromJKO.xlsx")
source_name = "JKO"

sources = pd.read_csv('sources.csv')

for i in range(len(sources["sourceName"])):
    name = sources["sourceName"][i]
    if name == source_name:
        source_row = i

print("COLUMN DATA FOR SOURCE:")
print(sources.iloc[source_row])
#TODO: Use the source data in place of hardcoded file names

#Dictionary with unique IDS as keys and another dictionary with important information as values
ids = dict()

#Groups rows by ID
group_by_id = JKOdf.groupby('EDIPI')

#Loops through the rows for each person
for idRows in group_by_id:
    edipi = idRows[0]
    grouped_rows = idRows[1]

    #Create a dictionary for this person with informatin about them
    ids[edipi] = dict()

    #Store ERIPI, name, and category
    ids[edipi]["EDIPI"] = edipi
    ids[edipi]["First Name"] = grouped_rows["First Name"].iloc[0]
    ids[edipi]["Last Name"] = grouped_rows["Last Name"].iloc[0]
    ids[edipi]["Category"] = grouped_rows["Category"].iloc[0]

    course_names = list(grouped_rows["Course Name"])
    course_completed_dates = list(grouped_rows["Completed Dt"])
    course_due_dates = list(grouped_rows["Due Dt"])

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

# def pretty_print_dict(d, indent=0):
#    for key, value in d.items():
#       print('\t' * indent + str(key))
#       if isinstance(value, dict):
#          pretty_print_dict(value, indent+1)
#       else:
#          print('\t' * (indent+1) + str(value))

# pretty_print_dict(ids)

output = pd.DataFrame(ids.values())

with pd.ExcelWriter('output.xlsx') as writer:
    output.to_excel(writer)
    