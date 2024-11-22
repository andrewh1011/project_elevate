# Project Elevate
### By Andrew Hartmann and Nicholas Fletcher

## Problem Overview

The Medical Group at Scott Air Force Base needs a system that outputs a report card for names and due dates for electronic training. Currently, this training data is pulled from many different sources and manually added to Excel. This process is very time consuming, and the team would like to automate this process.

## Description

We created a Python application with a UI interface. This interface allows for the importing of multiple training data files, and outputs an organized Excel file with important information.

### Libraries Used

    • PyQt5 - User interface
    • Pandas - Data manipulation & output formatting
    • thefuzz - Name matching
    • XlsxWriter - Output coloring

### How to Use

The application requires Excel (.xlsx) files from the training sources. You can import these files by clicking the "Import" button. 

Once imported, the application will ask you which source they came from (ie JKO, myLearning, ect.). Please choose the correct source from the dropdown menu. 

If the source is not in the dropdown menu or a source changes format, you can manually add a new data souce with the "Add Source" button.

Import as many files as necessary. Once all files have been added, click the "Create Output" button. This will generate an output in an Excel file (output.xlsx) in the same directory as the application.

The colors of the output has meaning:

    • Blue: important information about the trainees

Courses section:

      • Green: Course is assigned and completed on time
      • Yellow: Course is assigned and has not been completed yet, and it is not past the due date
      • Red: Course is assigned and not completed (if empty), or has been completed late (if there is a date)
      • Grey: Course has not been assigned to this person

Adding a Source:

A portion of the application allows for adding a new data source. Enter the index (starting from 0) of the important columns in the new data source so the application knows where to find them.

For example, let's say there is a data source with the following columns in the order:

Last Name, First Name, EDIPI, Category, Course Name, Completed Dt, Due Dt

'Last Name' is in column 0, 'First Name' is in column 1, DODID is in column 2 and so on.

The required entries are the name of the source, first name, due date, completed date, and course name. If the first name and last name columns are combined into one name column, enter the index of the name column in the 'First Name' column.

## Installation and Running Program

The main program is located in the src/code directory and is called "program.py." To run the application, simply cd into that directory and type:

    python program.py

Intalling dependencies...
