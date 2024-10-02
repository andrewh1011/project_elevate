from PyQt5.QtWidgets import *
import sys
from first import Ui_Dialog


class Ui(QDialog):
	def __init__(self):
		super(Ui, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.import_clicked)

	def import_clicked(self):
		file = QFileDialog.getOpenFileName(self, "Add Source", "/~", "Spreadsheets(*.csv *.xlsv *.txt)")
		print(file[0])


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Ui()
	window.show()
	sys.exit(app.exec_())