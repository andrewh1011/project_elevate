from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class FirstWindow(QMainWindow):
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Project Elevate")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Add Data")
        self.b1.clicked.connect(self.click_button)


    def click_button(self):
        self.label.setText("Button clicked")
        self.update()
    
    def update(self):
        print("change occured")

def window():
    app = QApplication(sys.argv)
    win = FirstWindow()
    win.show()
    sys.exit(app.exec_())

window()