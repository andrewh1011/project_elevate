from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QListWidget, QListWidgetItem, QInputDialog, QMessageBox, QLineEdit
import sys
from uiFile import Ui_Dialog
from addSource import Ui_AddWindow
from settingsUI import Ui_AddWindow as SettingUi_AddWindow
from manageSources import *
from manageSettings import *
from parsing import *

class MainUI(QMainWindow):
	
	def __init__(self):
		super(MainUI, self).__init__()

		
		self.fileNames = {} # maps fileNames to (fullFilePath, system) -> a tuple with important information about the file
		self.sources = None # this is a pandas dataframe. Each row's index is the source name. call the refresh_sources() anytime an update to the source storage file is made.
		
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.ui.sourceList.itemDoubleClicked.connect(self.source_clicked)
		self.ui.fileList.itemClicked.connect(self.file_clicked)

		self.ui.importButton.clicked.connect(self.import_clicked)
		self.ui.deleteFileBtn.clicked.connect(self.delete_file_clicked)
		self.ui.deleteSourceBtn.clicked.connect(self.delete_source_clicked)
		self.ui.addSourceBtn.clicked.connect(self.open_add_source_window)
		self.ui.settingsBtn.clicked.connect(self.open_settings_window)
		self.ui.startBtn.clicked.connect(self.start_btn_clicked)
		
		self.refresh_sources()

		self.ui.tutorialBtn.clicked.connect(self.open_tutorial)
		with open("../appStorage/generalAppInstructions.txt", "r") as file:
			self.tutorial_text = file.read()

	def name_match_confirmer(self):
		def nameMatchConfirmInner(name1, name2):
			choice = QMessageBox.question(self, 'Name Match Detected', name1 + " appears to match " + name2 + ". Proceed to combine these into one person record?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
			if choice == QMessageBox.Yes:
				return True
			else:
				return False
		return nameMatchConfirmInner

	def start_btn_clicked(self):
		keys = self.fileNames.keys()
		if len(keys) >	0:
			try:
				buildOutput(self.fileNames.values(), self.name_match_confirmer())
				self.ui.actionLabel.setText("Output generated in 'output.xlsx' file.")	
			except Exception as e:
				self.ui.actionLabel.setText("Parsing/Generation Error: " + str(e))
				print(str(e))
		else:
			self.ui.actionLabel.setText("Please provide at least one file for the report generation.")	

	def source_clicked(self, item):
		source_name = item.text()
		self.window = AddSourceUI(self)
		self.window.show_source_clicked(source_name, self.sources)
		self.window.show()

	def delete_all_files_with_source(self, sName):
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

	def confirm_delete_files_from_source(self, sName):
		choice = QMessageBox.question(self, 'Confirmation', "Deleting a source will delete all the files currently mapped to this source in the current session. Are you sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		return choice

	def refresh_sources(self):
		self.ui.sourceList.clear()
		self.sources = buildSourceDataFromFile()
		if not self.sources.empty:
			for source in self.sources[SourceFileColumns.sourceName.value].to_list():
				itm = QListWidgetItem(source)
				itm.setTextAlignment(QtCore.Qt.AlignCenter)
				self.ui.sourceList.addItem(itm)

	def delete_source_clicked(self):
		itm = self.ui.sourceList.currentItem()
		if (not self.sources.empty) and itm:
			sName = itm.text()
			choice = self.confirm_delete_files_from_source(sName)
			if choice == QMessageBox.Yes:
				ret = deleteSourceFromFile(sName)
				if ret:
					self.refresh_sources()
					self.delete_all_files_with_source(sName)
				else:
					self.ui.actionLabel.setText("Could not delete source" + sName)

	def open_add_source_window(self):
		self.window = AddSourceUI(self)
		self.window.show()
	
	def open_settings_window(self):
		self.window = AddSettingUI(self)
		self.window.show_settings()
		self.window.show()

	def delete_file_clicked(self):
		if self.fileNames:
			row = self.ui.fileList.currentRow()
			if row > -1:
				itm = self.ui.fileList.currentItem()
				self.ui.fileList.takeItem(row)
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
			source, ok_pressed = QInputDialog.getItem(self, "Source Selection", "Select Source:", self.sources[SourceFileColumns.sourceName.value].to_list(), 0, False)
		
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
			itm.setTextAlignment(QtCore.Qt.AlignCenter)
			self.ui.fileList.addItem(itm)

	def open_tutorial(self):
		instructions = QMessageBox(self)
		instructions.setIcon(QMessageBox.Information)
		instructions.setWindowTitle("Tutorial")
		instructions.setText(self.tutorial_text)
		instructions.exec_()

	def closeEvent(self, event): 
		for window in QApplication.topLevelWidgets(): 
			window.close()

class AddSourceUI(QMainWindow):
	def __init__(self, mainWindow):
		super(AddSourceUI, self).__init__()

		self.mainWindow = mainWindow
		self.ui = Ui_AddWindow()
		self.ui.setupUi(self)

		self.ui.saveSourceBtn.clicked.connect(self.save_source_clicked)
		
		self.ui.tutorialBtn.clicked.connect(self.open_tutorial)
		with open("../appStorage/addSourceInstructions.txt", "r") as file:
			self.add_tutorial_text = file.read()

	def show_source_clicked(self, source_name, sources):
		cols = list(sources.columns)
		for column in cols:
			val = sources.loc[source_name, column]
			inputField = self.findChild(QLineEdit, column)
			if inputField:
				if val != notUsedNumber:
					inputField.setText(str(val))
				else:
					inputField.setText("")
		
	def return_to_main_window(self):
		self.mainWindow.refresh_sources()
		self.close()

	def open_tutorial(self):
		instructions = QMessageBox(self)
		instructions.setIcon(QMessageBox.Information)
		instructions.setWindowTitle("Tutorial")
		instructions.setText(self.add_tutorial_text)
		instructions.exec_()

	#assumes all number columns have already been verified
	def package_source_form(self):
		dict = {}
		for sourceColumn in SourceFileColumns:
			inputField = self.findChild(QLineEdit, sourceColumn.value)
			if not sourceColumn in dict.keys():
				if sourceColumn.value == SourceFileColumns.sourceName.value:
					dict[sourceColumn.value] = inputField.text()
				else:
					dict[sourceColumn.value] = notUsedNumber if inputField.text() == "" else int(inputField.text())
		return dict

	def save_source_clicked(self):
		for sourceColumn in RequiredSourceFileColumns:
			inputField = self.findChild(QLineEdit, sourceColumn.value)
			if inputField:
				if inputField.text() == "":
					self.ui.actionLabel.setText("REQUIRED COLUMN " + inputField.objectName() + " NEEDS NON-EMPTY INPUT")
					return False
		
		#all columns besides sourceName should be a number(index).
		for sourceColumn in SourceFileColumns:
			inputField = self.findChild(QLineEdit, sourceColumn.value)
			if inputField:
				if inputField.text() != "" and sourceColumn.value != SourceFileColumns.sourceName.value:

					try:
						converted = int(inputField.text())
						if converted < 0:
							self.ui.actionLabel.setText("INPUT COLUMN " + inputField.objectName() + " HAS INVALID NUMBER")
							return False

					except ValueError:
						self.ui.actionLabel.setText("INPUT COLUMN " + inputField.objectName() + " NEEDS A NUMBER")
						return False
	
		formData = self.package_source_form()

		for sourceColumn in SourceFileColumns:			
			if sourceColumn.value != SourceFileColumns.sourceName.value and sourceColumn.value != SourceFileColumns.skipRows.value:
				for sourceColumnInner in SourceFileColumns:
					if sourceColumnInner.value != SourceFileColumns.sourceName.value and sourceColumnInner.value != SourceFileColumns.skipRows.value and sourceColumnInner.value != sourceColumn.value:	
						if formData[sourceColumn.value] == formData[sourceColumnInner.value] and formData[sourceColumn.value] != notUsedNumber:
							self.ui.actionLabel.setText("DUPLICATE COLUMN INDICES ASSIGNED")
							return False
	

		ret = addSourceToFile(formData)
		if ret:
			self.return_to_main_window()
			return True
		else:
			self.mainWindow.ui.actionLabel.setText("Source could not be added")
			self.return_to_main_window()
			return False

class AddSettingUI(QMainWindow):
	def __init__(self, mainWindow):
		super(AddSettingUI, self).__init__()

		self.mainWindow = mainWindow
		self.ui = SettingUi_AddWindow()
		self.ui.setupUi(self)

		self.ui.saveBtn.clicked.connect(self.save_setting_clicked)
		
		self.ui.tutorialBtn.clicked.connect(self.open_tutorial)
		with open("../appStorage/settingsInstructions.txt", "r") as file:
			self.add_tutorial_text = file.read()

	def show_settings(self):
		settings = buildSettingsDataFromFile()
		cols = list(settings.index)
		for column in cols:
			val = settings.loc[column]
			inputField = self.findChild(QLineEdit, column)
			if inputField:
				inputField.setText(str(val))
						
	def return_to_main_window(self):
		self.close()

	def open_tutorial(self):
		instructions = QMessageBox(self)
		instructions.setIcon(QMessageBox.Information)
		instructions.setWindowTitle("Tutorial")
		instructions.setText(self.add_tutorial_text)
		instructions.exec_()

	#assumes all number columns have already been verified
	def package_setting_form(self):
		dict = {}
		for setColumn in SettingsFileColumns:
			inputField = self.findChild(QLineEdit, setColumn.value)
			if not setColumn in dict.keys():
				dict[setColumn.value] = int(inputField.text())
		return dict

	def save_setting_clicked(self):
		for setColumn in RequiredSettingsFileColumns:
			inputField = self.findChild(QLineEdit, setColumn.value)
			if inputField:
				if inputField.text() == "":
					self.ui.actionLabel.setText("REQUIRED COLUMN " + inputField.objectName() + " NEEDS NON-EMPTY INPUT")
					return False

		nameThresholdField = self.findChild(QLineEdit, SettingsFileColumns.nameMatchThreshold.value)
		if nameThresholdField:
			if nameThresholdField.text() != "":
				try:
					converted = int(nameThresholdField.text())
					if converted < 0 or converted > 100:
						self.ui.actionLabel.setText("Name Match Threshold Value must be greater than or equal to 0 and less than or equal to 100.")
						return False

				except ValueError:
					self.ui.actionLabel.setText("Name Match Threshold Value must be a number.")
					return False
		
		autoThresholdField = self.findChild(QLineEdit, SettingsFileColumns.autoMatchThreshold.value)
		if autoThresholdField:
			if autoThresholdField.text() != "":
				try:
					converted = int(autoThresholdField.text())
					if converted < 0 or converted > 100:
						self.ui.actionLabel.setText("Auto Name Match Threshold Value must be greater than or equal to 0 and less than or equal to 100.")
						return False

				except ValueError:
					self.ui.actionLabel.setText("Auto Name Match Threshold Value must be a number.")
					return False
		
	
	
		formData = self.package_setting_form()
		ret = addSettingsToFile(formData)
		if ret:
			self.return_to_main_window()
			return True
		else:
			self.mainWindow.ui.actionLabel.setText("Settings could not be updated.")
			self.return_to_main_window()
			return False

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainUI()
	window.show()
	sys.exit(app.exec_())