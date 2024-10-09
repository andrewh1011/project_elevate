from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QListWidget, QListWidgetItem, QInputDialog
import sys
from multipleFiles import Ui_Dialog
from manageSources import *

class Ui(QMainWindow):
	
	def __init__(self):
		super(Ui, self).__init__()

		
		self.fileNames = {} # maps fileNames to (fullFilePath, system) -> a tuple with important information about the file
		self.sources = buildSourceDataFromFile() # this is a pandas dataframe. Each row's index is the source name. call the buildSourceDataFromFile() anytime an update to the source storage file is made.
		
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.importButton.clicked.connect(self.import_clicked)
		self.ui.fileList.itemClicked.connect(self.file_clicked)
		self.ui.sourceList.itemClicked.connect(self.source_clicked)
		self.ui.deleteFileBtn.clicked.connect(self.delete_file_clicked)
		self.ui.deleteSourceBtn.clicked.connect(self.delete_source_clicked)
		self.ui.saveSourceBtn.clicked.connect(self.save_source_clicked)
		self.refresh_sources()

	def refresh_sources(self):
		self.ui.sourceList.clear()
		self.sources = buildSourceDataFromFile()
		for source in self.sources.index.values:
			itm = QListWidgetItem(source)
			self.ui.sourceList.addItem(itm)

	def delete_source_clicked(self):
		if self.sources:
			row = self.ui.sourceList.currentRow()
			itm = self.ui.sourceList.currentItem()
			self.ui.sourceList.takeItem(row)
			self.ui.actionLabel.setText("Deleted source" + itm.text())
			del self.sources[itm.text()]

	def source_clicked(self, item):
		self.ui.actionLabel.setText(item.text())

	def save_source_clicked(self):
		name = self.ui.sourceNameEdit.text()
		nameCol = self.ui.nameColEdit.text()
		dateCol = self.ui.dateColEdit.text()
		idCol = self.ui.idColEdit.text()
		if name != "" and nameCol != "" and dateCol != "":
			if not self.sources.empty and name in self.sources.index.values:
				self.ui.actionLabel.setText("DUPLICATE SOURCE")
			else:
				self.ui.actionLabel.setText("source " + name + " saved")
				addSourceToFile(name, nameCol,dateCol,idCol)
				self.refresh_sources()
		else:
			self.ui.actionLabel.setText("SOURCE NEEDS NAME, NAME_COL, and DATE_COL")

	def delete_file_clicked(self):
		if self.fileNames:
			row = self.ui.fileList.currentRow()
			itm = self.ui.fileList.currentItem()
			self.ui.fileList.takeItem(row)
			self.ui.actionLabel.setText("Deleted" + itm.text())
			del self.fileNames[itm.text()]

	
	def import_clicked(self):
		file = QFileDialog.getOpenFileName(self, "Add Source", "/~", "Spreadsheets(*.csv *.xlsv *.txt)")
		system = self.get_source()

		if file and system:
			fileFullPath = file[0]
			fileName = file[0].rsplit('/', 1)[-1]
			self.add_to_file_list(fileName, fileFullPath, system)

	def get_source(self):
		if self.sources:
			system, ok_pressed = QInputDialog.getItem(self, "System Selection", "Select System:", self.sources, 0, False)
		
			if ok_pressed:
				return system
		
			#User clicked cancel
			return None
		else:
			self.ui.actionLabel.setText("Please create a source")

	def file_clicked(self, item):
		self.ui.actionLabel.setText(self.fileNames[item.text()][0])

	def add_to_file_list(self, name, path, system):
		
		if name in self.fileNames:
			self.ui.actionLabel.setText("DUPLICATE")
		else:
			self.fileNames[name] = (path, system)
			itm = QListWidgetItem(name)
			self.ui.fileList.addItem(itm)
			self.ui.actionLabel.setText("ADDED FILE" + itm.text())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Ui()
	window.show()
	sys.exit(app.exec_())