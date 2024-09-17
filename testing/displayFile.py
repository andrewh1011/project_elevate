import pandas as pd
from PyQt5.QtWidgets import QApplication, QLabel

docE = pd.read_excel('SimpleTest.xlsx', header=None)

#print(docE)

####################################################

docC = pd.read_csv('SimpleTest.csv', header=None)

#print(docC)

####################################################
app = QApplication([])
label = QLabel(docE.to_string())
label.show()
app.exec()