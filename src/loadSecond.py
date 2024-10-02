from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel
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
        if file:
            self.ui.label.setText("File chosen: " + file[0].rsplit('/', 1)[-1])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())