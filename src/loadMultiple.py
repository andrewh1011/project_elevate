from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QListWidget, QListWidgetItem, QInputDialog
import sys
from multipleFiles import Ui_Dialog

class Ui(QMainWindow):
	
	def __init__(self):
		super(Ui, self).__init__()

		self.fileNames = {} # maps fileNames to (fullFilePath, system) -> a tuple with important information about the file
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.ui.importButton.clicked.connect(self.import_clicked)
		self.ui.listWidget.itemClicked.connect(self.item_clicked)
		self.ui.pushButton.clicked.connect(self.delete_clicked)

		self.ui.label.setText("File chosen: ")

	def delete_clicked(self):
		if self.fileNames:
			row = self.ui.listWidget.currentRow()
			itm = self.ui.listWidget.currentItem()
			self.ui.listWidget.takeItem(row)
			del self.fileNames[itm.text()]
	
	def import_clicked(self):
		file = QFileDialog.getOpenFileName(self, "Add Source", "/~", "Spreadsheets(*.csv *.xlsv *.txt)")
		system = self.get_system()

		if file and system:
			fileFullPath = file[0]
			fileName = file[0].rsplit('/', 1)[-1]
			self.ui.label.setText("File chosen: " + fileName)
			self.add_to_list(fileName, fileFullPath, system)

	def get_system(self):
		systems = ["System 1", "System 2", "System 3", "System 4", "System 5", "System 6"]
		system, ok_pressed = QInputDialog.getItem(self, "System Selection", "Select System:", systems, 0, False)
		
		if ok_pressed:
			return system
		
		#User clicked cancel
		return None

	def item_clicked(self, item):
		self.ui.label.setText(self.fileNames[item.text()][0])

	def add_to_list(self, name, path, system):
		
		if name in self.fileNames:
			self.ui.label.setText("DUPLICATE")
			print(self.fileNames[name])
		else:
			self.fileNames[name] = (path, system)
			itm = QListWidgetItem(name)
			self.ui.listWidget.addItem(itm)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Ui()
	window.show()
	sys.exit(app.exec_())