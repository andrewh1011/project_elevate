from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QInputDialog
import sys
from second import Ui_Dialog

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.importButton.clicked.connect(self.import_clicked)
        self.ui.label.setText("File chosen: ")

    def import_clicked(self):
        file = QFileDialog.getOpenFileName(self, "Add Source", "/~", "Spreadsheets(*.csv *.xlsv *.txt)")

        system = self.get_system()

        if file and system:
            self.ui.label.setText("File chosen: " + file[0].rsplit('/', 1)[-1])


       

    def get_system(self):
        systems = ["System 1", "System 2", "System 3", "System 4", "System 5", "System 6"]
        
        system, ok_pressed = QInputDialog.getItem(self, "Select System", "Systems", systems, 0, False)
        
        if ok_pressed:
            return system

        return None



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())