from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QListWidget, QListWidgetItem, QInputDialog,QMessageBox, QLineEdit
import sys
from PyQt5 import Qt
from uiFile import Ui_Dialog
from manageSources import *

class Ui(QMainWindow):
	
	def __init__(self):
		super(Ui, self).__init__()

		
		self.fileNames = {} # maps fileNames to (fullFilePath, system) -> a tuple with important information about the file
		self.sources = None # this is a pandas dataframe. Each row's index is the source name. call the refresh_sources() anytime an update to the source storage file is made.
		
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.importButton.clicked.connect(self.import_clicked)
		self.ui.fileList.itemClicked.connect(self.file_clicked)
		self.ui.sourceList.itemClicked.connect(self.source_clicked)
		self.ui.deleteFileBtn.clicked.connect(self.delete_file_clicked)
		self.ui.deleteSourceBtn.clicked.connect(self.delete_source_clicked)
		self.ui.saveSourceBtn.clicked.connect(self.save_source_clicked)
		self.refresh_sources()

	def packageSourceForm(self):
		dict = {}
		for sourceColumn in SourceFileColumns:
			inputField = self.findChild(QLineEdit, sourceColumn.value)
			if inputField:
				if not sourceColumn in dict.keys():
					dict[sourceColumn.value] = inputField.text()
		return dict
				

	def deleteAllFilesWithSource(self, sName):
		fileDict = self.fileNames
		fileListWidget = self.ui.fileList
		remFiles = []
		for fName in fileDict.keys():
			source = (fileDict[fName])[1]
			if source == sName:
				itm = fileListWidget.findItems(fName,Qt.Qt.MatchExactly)[0]
				fileListWidget.takeItem(fileListWidget.row(itm))
				remFiles.append(fName)
		for file in remFiles:
			del fileDict[file]

	def confirmDeleteFilesFromSource(self, sName):
		choice = QMessageBox.question(self, 'Confirmation', "Deleting a source will delete all the files currently mapped to this source in the current session. Are you sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		return choice

	def refresh_sources(self):
		self.ui.sourceList.clear()
		self.sources = buildSourceDataFromFile()
		if not self.sources.empty:
			for source in self.sources[SourceFileColumns.sourceName.value].to_list():
				itm = QListWidgetItem(source)
				self.ui.sourceList.addItem(itm)

	def delete_source_clicked(self):
		itm = self.ui.sourceList.currentItem()
		if (not self.sources.empty) and itm:
			sName = itm.text()
			choice = self.confirmDeleteFilesFromSource(sName)
			if choice == QMessageBox.Yes:
				ret = deleteSourceFromFile(sName)
				if ret:
					self.ui.actionLabel.setText("Deleted source" + sName)
					self.refresh_sources()
					self.deleteAllFilesWithSource(sName)
				else:
					self.ui.actionLabel.setText("Could not delete source" + sName)

	def source_clicked(self, item):
		sourceName = item.text()
		self.refresh_sources()
		cols = list(self.sources.columns)
		for column in cols:
			val = self.sources.loc[sourceName, column]
			inputField = self.findChild(QLineEdit, column)
			if inputField:
				inputField.setText(str(val))
			

	def save_source_clicked(self):
		for sourceColumn in RequiredSourceFileColumns:
			inputField = self.findChild(QLineEdit, sourceColumn.value)
			if inputField:
				if inputField.text() == "":
					self.ui.actionLabel.setText("REQUIRED COLUMN " + inputField.objectName() + " NEEDS NON-EMPTY INPUT")
					return False
		formData = self.packageSourceForm()
		ret = addSourceToFile(formData)
		if ret:
			self.ui.actionLabel.setText("source updated")
			self.refresh_sources()
			return True
		else:
			self.ui.actionLabel.setText("source could not be updated")
			return False

	def delete_file_clicked(self):
		if self.fileNames:
			row = self.ui.fileList.currentRow()
			itm = self.ui.fileList.currentItem()
			self.ui.fileList.takeItem(row)
			self.ui.actionLabel.setText("Deleted" + itm.text())
			del self.fileNames[itm.text()]

	
	def import_clicked(self):
		file = QFileDialog.getOpenFileName(self, "Add Source", "/~", "Spreadsheets(*.csv *.xlsx *.txt)")

		if file[0]:
			system = self.get_source()
			if system:
				fileFullPath = file[0]
				fileName = file[0].rsplit('/', 1)[-1]
				self.add_to_file_list(fileName, fileFullPath, system)

	def get_source(self):
		if not self.sources.empty:
			source, ok_pressed = QInputDialog.getItem(self, "System Selection", "Select System:", self.sources[SourceFileColumns.sourceName.value].to_list(), 0, False)
		
			if ok_pressed:
				return source
		
			#User clicked cancel
			return None
		else:
			self.ui.actionLabel.setText("Please create a source")

	def file_clicked(self, item):
		self.ui.actionLabel.setText(self.fileNames[item.text()][0])

	def add_to_file_list(self, name, path, system):
		
		if name in self.fileNames:
			self.ui.actionLabel.setText("Duplicate file")
		else:
			self.fileNames[name] = (path, system)
			itm = QListWidgetItem(name)
			self.ui.fileList.addItem(itm)
			self.ui.actionLabel.setText("Added file: " + itm.text())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Ui()
	window.show()
	sys.exit(app.exec_())