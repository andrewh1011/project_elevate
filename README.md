# Project Elevate
### By Andrew Hartmann and Nicholas Fletcher

## Problem Overview

The Medical Group at Scott Air Force Base needs a system that outputs a report card for names and due dates for electronic training. Currently, this training data is pulled from many different sources and manually added to Excel. This process is very time consuming, and the team would like to automate this process.

## Description

We created a Python application with a UI interface. This interface allows for the importing of multiple training data files from different sources, and outputs an organized Excel file with important information. We allow for adding multiple custom courses with different fortatting.

### Libraries Used

    • PyQt5(Version 5.15.11) - User interface
    • pandas(Version 2.2.2) - Data manipulation & output formatting
    • thefuzz(Version 0.22.1) - Name matching
    • XlsxWriter(Version 3.2.0) - Library used by pandas excel writer to output/read excel files. 
    • openpyxl(Version 3.1.5) - Library used by pandas excel writer to output/read excel files. 

## Installation and Running Program
There are two ways to use this program. Either you can run it with the python interpreter or compile it and run it as an executable. Regardless of which way you choose to run it, you will need python installed.

Additionally, we recommend using a virtual environment alongside python. This will allow you to make sure the library versions you are using are the same ones we tested and developed this app to use and that other python programs on the computer that need different versions of libraries will not interfere with this app. 

### Creating the virtual environment
1) navigate to the code directory(src/code).
2) Run command: "python -m venv .venv"
3) From the code directory, run command: ".venv\Scripts\activate"
4) Now that you are in the virtual environment, run command: "python -m pip install --upgrade pip"
5) For each of the required libraries(and versions) above, run the command: "pip install -Iv lib==version" where lib is the library name and version is the version of that library.
6) Your virtual environment should now have all the required libraries needed to run the app. You can leave the virtual environment by running the command "deactivate"


The main program is located in the src/code/ directory and is called "program.py". To run the application, navigate into the src/code/ directory and type:

    python program.py

Make sure all the libraries are installed. You may need to run:

    pip install PyQt5
    pip install Pandas
    pip install thefuzz
    pip install XlsxWriter
    (if compiling to executable) pip install openpyxl

### Executable
    ensure libraries above have been installed with pip. Additionally, ensure the directory these libraries are stored in is included in your system PATH(so that the compiler used next can find them).
    -run command: pip install -U nuitka
    Note: before proceeding, make sure your python app is downloaded directly from the python site and not from the windows app store. The nuitka compiler enforces this.
    -navigate to directory where source code is kept for this app.
    -run command: python -m nuitka program.py --standalone --plugin-enable=pyqt5 --include-module=pandas --include-module=thefuzz --onefile --include-module=openpyxl
    This will take a pretty long time. 
    Once the executable has been compiled, it should stay in this source code directory so that the app knows where the instruction/storage files it needs to run are.
    

## How to Use

The application requires Excel (.xlsx) files from the training sources. You can import these files by clicking the "Import" button. 

Once imported, the application will ask you which source they came from (ie JKO, myLearning, ect.). Please choose the correct source from the dropdown menu. 

If the source is not in the dropdown menu or a source changes format, you can manually add a new data souce with the "Add Source" button.

Import as many files as necessary. Once all files have been added, click the "Create Output" button. This will generate an output in an Excel file (output.xlsx) in the same directory as the application.

The colors of the output has meaning:

    • Blue: important information about the trainees

### Courses section:

      • Green: Course is assigned and completed on time
      • Yellow: Course is assigned and has not been completed yet, and it is not past the due date
      • Red: Course is assigned and not completed (if empty), or has been completed late (if there is a date)
      • Grey: Course has not been assigned to this person

### Adding a Source:

A portion of the application allows for adding a new data source. Enter the index (starting from 0) of the important columns in the new data source so the application knows where to find them.

For example, let's say there is a data source with the following columns in the order:

Last Name, First Name, EDIPI, Category, Course Name, Completed Dt, Due Dt

'Last Name' is in column 0, 'First Name' is in column 1, DODID is in column 2 and so on.

The required entries are the name of the source, first name, due date, completed date, and course name. If the first name and last name columns are combined into one name column, enter the index of the name column in the 'First Name' column.
