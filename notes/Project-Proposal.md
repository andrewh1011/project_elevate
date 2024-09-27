**Andrew Hartmann & Nicholas Fletcher**

# Project Elevate

## **27th September 2024**

# **OVERVIEW**

The Medical Group at Scott Air Force Base needs a system that outputs a report card for names and due dates for electronic training. Currently, this training data is pulled from many different sources and manually added to Excel. This process is very time consuming, and the team would like to automate this process.

# **Required Application Features**

- There will be a simple user interface that allows the user to easily input the files to the program  
- We need a way to identify which training system each file comes from to analyze accordingly (each system contains different data formatting)  
- The program will need to take each input file once each schema has been figured out and find a way to combine all of the data into one file in a consistent way  
- The program will need to take this joined data and make a report that highlights each person’s status on a given training module  
- There will need to be a way to export this final report, starting with excel sheets

# **Additional Application Features (if time permits)**

- Expand options for exporting the report (ie csv, pdf, email)  
- Expand options for importing files

# **Technology Stack**

- *Main application* \- Python (pending approval)  
  - Pandas library for data processing  
  - PyQT5 for user interface  
- *Displaying final report*  \- Excel  
- *Version control and task tracking* \- GitHub  
- *Note taking \- Google Docs*

# **Testing**

- Will feed our program the provided input sample data and compare the result of our program with the behavior of Technical Sergeant West’s existing program.  
- We can potentially coordinate with Technical Sergeant West or someone else from the medical team and have them use our program to test.

# **Estimated Timeline**

- Create a simple user interface that allows the user to select a file. The program should then be able to read this file. (1 week)  
- Develop a way to analyze the contents of each of the 6 different systems. (2 weeks)  
- Develop a way to combine the standardized content of each individual system input into one report. (2 weeks)  
- Develop export system for excel. (2 days)  
- Enhancements will use any remaining time after the above points.  
- Testing will be done throughout the semester

# **Sharing the project**

- We will email them the final program. If there is a separate executable and source code we will give them both. We will also include a writeup for any necessary instructions for using the program.
