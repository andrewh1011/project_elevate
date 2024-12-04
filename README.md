# Project Elevate
### By Andrew Hartmann and Nicholas Fletcher

## Problem Overview

The Medical Group at Scott Air Force Base needs a system that outputs a report card for names and due dates for electronic training. Currently, this training data is pulled from many different sources and manually added to Excel. This process is very time consuming, and the team would like to automate this process.

## Description

We created a Python application with a UI interface. This interface allows for the importing of multiple training data files from different sources, and outputs an organized Excel file with important information. We allow for adding multiple custom courses with different formatting.

### Libraries Used

    • PyQt5(Version 5.15.11) - User interface
    • pandas(Version 2.2.2) - Data manipulation & file reading/writing
    • thefuzz(Version 0.22.1) - Name matching
    • XlsxWriter(Version 3.2.0) - Library used by pandas excel writer to output/read excel files. 
    • openpyxl(Version 3.1.5) - Library used by pandas excel writer to output/read excel files. 

## Installation and Running Program
There are two ways to use this program. Either you can run it with the python interpreter or compile it and run it as an executable. Regardless of which way you choose to run it, you will need python installed.

Additionally, we recommend using a virtual environment alongside python. This will allow you to make sure the library versions you are using are the same ones we tested and developed this app to use and that other python programs on the computer that need different versions of libraries will not interfere with this app. 

### Creating the Virtual Environment
1) navigate to the code directory(src/code).
2) Run command: "python -m venv .venv"
3) From the code directory, run command: ".venv\Scripts\activate"
4) Now that you are in the virtual environment, run command: "python -m pip install --upgrade pip"
5) For each of the required libraries(and versions) above, run the command: "pip install -Iv lib==version" where lib is the library name and version is the version of that library.
6) Your virtual environment should now have all the required libraries needed to run the app. You can leave the virtual environment by running the command "deactivate"

### Running the App with the Python Interpreter
1) navigate to the code directory(src/code)
2) Enter the virtual environment with the command: ".venv\Scripts\activate"
3) Run command: "python program.py"

### Running the App as an Executable
We have provided the app as an executable(program.exe in the code directory), but the executable may not work on your machine if it has a different architecture. This means you may have to recompile the app if you want to use it as an executable. You may also want to make changes to the source code, which would require recompiling if you want to use the app as an executable.
To recompile:
1) navigate to the code directory(src/code)
2) Enter the virtual environment with the command: ".venv\Scripts\activate"
3) run command: "pip install -U nuitka". Note: before proceeding, make sure your python app is downloaded directly from the python site and not from the windows app store. The nuitka compiler enforces this.
4) run command: python -m nuitka program.py --standalone --plugin-enable=pyqt5 --include-module=pandas --include-module=thefuzz --onefile --include-module=openpyxl --include-module=XlsxWriter
5) At this point the executable(program.exe) will be compiled and you can run it however you normally run executable programs.
  
## Using the App
Each important section of the app will have an instruction button associated with it. Clicking this button will cause a popup with instructions to be displayed that give information about that section of the app.
If you wish to read the instructions without running the app, they can be found in the src/appStorage directory.


