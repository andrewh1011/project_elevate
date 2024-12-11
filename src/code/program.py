from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QMainWindow,QPlainTextEdit, QApplication, QPushButton, QFileDialog, QLabel, QListWidget, QListWidgetItem, QInputDialog, QMessageBox, QLineEdit
import sys, os
from uiFile import Ui_Dialog
from addSource import Ui_AddWindow
from settingsUI import Ui_AddWindow as SettingUi_AddWindow
from addTypeUI import Ui_AddWindow as TypeUi_AddWindow
from instructionUI import Ui_AddWindow as Inst_Window
from manageSources import *
from manageSettings import *
from manageTypes import *
from parsing import *

#make sure the directories of files needed by the app are resolved to be relative to the path of the current python file, NOT the cwd.
#cwd is not always guaranteed to be in the code dir, ie when using desktop icons.
baseDir = os.path.dirname(__file__)
genAppInstPath = os.path.join(baseDir, "../appStorage/generalAppInstructions.txt")
addSrcInstPath = os.path.join(baseDir, "../appStorage/addSourceInstructions.txt")
addSetInstPath = os.path.join(baseDir, "../appStorage/settingsInstructions.txt")
addTypeInstPath = os.path.join(baseDir, "../appStorage/typesInstructions.txt")

class MainUI(QMainWindow):
	
	def __init__(self):
		super(MainUI, self).__init__()
		self.fileNames = {} # maps fileNames to (fullFilePath, sourceName)
		
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.ui.sourceList.itemDoubleClicked.connect(self.source_clicked)
		self.ui.typeList.itemDoubleClicked.connect(self.type_clicked)
		self.ui.fileList.itemClicked.connect(self.file_clicked)
		self.ui.importButton.clicked.connect(self.import_clicked)
		self.ui.deleteFileBtn.clicked.connect(self.delete_file_clicked)
		self.ui.deleteSourceBtn.clicked.connect(self.delete_source_clicked)
		self.ui.addSourceBtn.clicked.connect(self.open_add_source_window)
		self.ui.addTypeBtn.clicked.connect(self.open_add_type_window)
		self.ui.deleteTypeBtn.clicked.connect(self.delete_type_clicked)
		self.ui.settingsBtn.clicked.connect(self.open_settings_window)
		self.ui.startBtn.clicked.connect(self.start_btn_clicked)
		self.refresh_sources()
		self.refresh_types()
		self.ui.tutorialBtn.clicked.connect(self.open_tutorial)
		

	#Prompts user to confirm to two names are the same person
	def name_match_confirmer(self):
		#returns (bool: yesAnswer, bool: keepGoing)
		def nameMatchConfirmInner(name1, name2):
			msgBox = QMessageBox()
			msgBox.setWindowTitle("Name Match Detected")
			msgBox.setText(name1 + " appears to match " + name2 + ". Proceed to combine these into one person record?")
			msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Close)
			choice = msgBox.exec_()
			if choice == QMessageBox.Close:
				return (False,False)
			else:
				if choice == QMessageBox.Yes:
					return (True,True)
				else:
					return (False, True)
		return nameMatchConfirmInner

	#Uses to parsing.py to build an output with the input files
	def start_btn_clicked(self):
		keys = self.fileNames.keys()
		if len(keys) >	0:
			#try:
			self.ui.actionLabel.setPlainText("Output generation started...")
			QApplication.processEvents()
			ret = buildOutput(self.fileNames.values(), self.name_match_confirmer())
			self.ui.actionLabel.setPlainText(ret)
			#except Exception as e:
			#	self.ui.actionLabel.setPlainText("Parsing/Generation Error: " + str(e))
		else:
			self.ui.actionLabel.setPlainText("Please provide at least one file for the report generation.")	

	def source_clicked(self, item):
		source_name = item.text()
		self.window = AddSourceUI(self)
		self.window.show_source_clicked(source_name)
		self.window.show()

	def type_clicked(self, item):
		type_name = item.text()
		self.window = AddTypeUI(self)
		self.window.show_type_clicked(type_name)
		self.window.show()

	#If a source is deleted, all files with the source must be deleted
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

	def default_all_sources_with_type(self, typeName):
		sources = buildSourceDataFromFile()
		for sourcek in sources.keys():
			sourceInfo = sources[sourcek]
			sourceType = sourceInfo[ExtraSourceFileColumns.typeName.value]
			if sourceType == typeName:
				sourceInfo[ExtraSourceFileColumns.typeName.value] = emptyTypeName
				addSourceToFile(sourceInfo)

	def confirm_delete_files_from_source(self, sName):
		choice = QMessageBox.question(self, 'Confirmation', "Deleting a source will delete all the files currently mapped to this source in the current session. Are you sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		return choice

	def confirm_edit_sources_of_type(self, sName):
		choice = QMessageBox.question(self, 'Confirmation', "Deleting a type will set any source using this type to use an empty type. Are you sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		return choice

	def refresh_sources(self):
		self.ui.sourceList.clear()
		sources = buildSourceDataFromFile()
		for source in sources.keys():
			itm = QListWidgetItem(source)
			itm.setTextAlignment(QtCore.Qt.AlignCenter)
			self.ui.sourceList.addItem(itm)
	
	def refresh_types(self):
		self.ui.typeList.clear()
		types = buildTypeDataFromFile()
		for typeR in types.keys():
				if typeR != emptyTypeName:
					itm = QListWidgetItem(typeR)
					itm.setTextAlignment(QtCore.Qt.AlignCenter)
					self.ui.typeList.addItem(itm)

	def delete_source_clicked(self):
		itm = self.ui.sourceList.currentItem()
		if itm:
			sName = itm.text()
			choice = self.confirm_delete_files_from_source(sName)
			if choice == QMessageBox.Yes:
				ret = deleteSourceFromFile(sName)
				if ret:
					self.refresh_sources()
					self.delete_all_files_with_source(sName)
				else:
					self.ui.actionLabel.setPlainText("Could not delete source" + sName)

	def delete_type_clicked(self):
		itm = self.ui.typeList.currentItem()
		if itm:
			tName = itm.text()
			choice = self.confirm_edit_sources_of_type(tName)
			if choice == QMessageBox.Yes:
				ret = deleteTypeFromFile(tName)
				if ret:
					self.refresh_types()
					self.default_all_sources_with_type(tName)
				else:
					self.ui.actionLabel.setPlainText("Could not delete type" + tName)

	def open_add_type_window(self):
		self.window = AddTypeUI(self)
		self.window.show()

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
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		files = QFileDialog.getOpenFileNames(self, "Add File", "/~", "Spreadsheets (*.xlsx)", options = options)
		if files and len(files) > 0 and files[0]:
			fileList = files[0]
			for file in fileList:
				fileFullPath = file
				fileName = file.rsplit('/', 1)[-1]

				system = self.get_source(fileName)
				if system:
					self.add_to_file_list(fileName, fileFullPath, system)
				else:
					break

	#Allows the user to tell us what source the file they imported is from
	def get_source(self, fileName):
		sources = buildSourceDataFromFile()
		if len(sources.keys()) > 0:
			source, ok_pressed = QInputDialog.getItem(self, "Source Selection", "Select Source for file " + fileName + ":", sources.keys(), 0, False)
			if ok_pressed:
				return source
			#User clicked cancel
			return None
		else:
			self.ui.actionLabel.setPlainText("Please create a source")

	def file_clicked(self, item):
		self.ui.actionLabel.setPlainText(self.fileNames[item.text()][0])

	def add_to_file_list(self, name, path, system):
		
		if name in self.fileNames:
			self.ui.actionLabel.setPlainText("Duplicate file")
		else:
			self.fileNames[name] = (path, system)
			itm = QListWidgetItem(name)
			itm.setTextAlignment(QtCore.Qt.AlignCenter)
			self.ui.fileList.addItem(itm)

	def open_tutorial(self):
		tutorialText = ""
		with open(genAppInstPath, "r") as file:
			tutorialText = file.read()
		self.window = InstructionUI(self,tutorialText)
		self.window.show()

	#If the main window is closed, close all other windows
	def closeEvent(self, event): 
		for window in QApplication.topLevelWidgets(): 
			window.close()

class InstructionUI(QMainWindow):
	def __init__(self, mainWindow, text):
		super(InstructionUI, self).__init__()

		self.mainWindow = mainWindow
		self.ui = Inst_Window()
		self.ui.setupUi(self)
		self.ui.instructionText.setPlainText(text)

#This window allows the user to edit and add a new source
class AddSourceUI(QMainWindow):
	def __init__(self, mainWindow):
		super(AddSourceUI, self).__init__()

		self.mainWindow = mainWindow
		self.ui = Ui_AddWindow()
		self.ui.setupUi(self)
		self.ui.saveSourceBtn.clicked.connect(self.save_source_clicked)
		self.ui.tutorialBtn.clicked.connect(self.open_tutorial)
		

		for rCol in RequiredSourceFileColumns:
			el = self.findChild(QLabel, rCol.value + "Label")
			el.setStyleSheet('color: red;')

		types = buildTypeDataFromFile()
		for ind in types.keys():
			self.ui.typeDdl.addItem(ind)
		self.populateDynamicCols(self.ui.typeDdl.currentText())

		self.ui.typeDdl.currentIndexChanged.connect(self.typeChanged)
		
	def clearDynamicCols(self):
		while self.ui.dynamicLabelVL.count():
			item = self.ui.dynamicLabelVL.takeAt(0)
			widget = item.widget()
			if widget is not None:
				widget.deleteLater()
		while self.ui.dynamicIndexVL.count():
			item = self.ui.dynamicIndexVL.takeAt(0)
			widget = item.widget()
			if widget is not None:
				widget.deleteLater()

	def typeChanged(self,ind):
		types = buildTypeDataFromFile()
		currType = self.ui.typeDdl.currentText()
		self.populateDynamicCols(currType)


	def populateDynamicCols(self, typeName):
		types = buildTypeDataFromFile()
		self.clearDynamicCols()
		if typeName != "" and typeName != emptyTypeName:
			customCols = str(types[typeName][TypeFileColumns.colList.value])
			colList = customCols.split(",")
			for col in colList:
				lab = QLabel()
				lab.setText(col + ":")
				lab.setStyleSheet('color: red;')
				lab.setObjectName(col + "Label")

				lEdit = QLineEdit()
				lEdit.setObjectName(col)
				self.ui.dynamicLabelVL.addWidget(lab)
				self.ui.dynamicIndexVL.addWidget(lEdit)

	def fillDynamicCol(self, columnName, columnIndex):
		for i in range(self.ui.dynamicIndexVL.count()):
			item = self.ui.dynamicIndexVL.itemAt(i)
			if item.widget() and item.widget().objectName() == columnName:
				el = item.widget()
				el.setText(columnIndex)
		
	#Fill out source values if source is clicked
	def show_source_clicked(self, source_name):
		sources = buildSourceDataFromFile()
		for column in SourceFileColumns:
			colName = column.value
			val = sources[source_name][colName]
			inputField = self.findChild(QLineEdit, colName)
			if inputField:
				inputField.setText(str(val))
				
		tName = sources[source_name][ExtraSourceFileColumns.typeName.value]
		self.ui.typeDdl.blockSignals(True)
		self.ui.typeDdl.setCurrentText(str(tName))
		self.populateDynamicCols(tName)
		tcols = sources[source_name][ExtraSourceFileColumns.typeCols.value]
		for col in tcols.keys():
			colIndex = tcols[col]
			self.fillDynamicCol(col,colIndex)
		self.ui.typeDdl.blockSignals(False)

	def return_to_main_window(self):
		self.mainWindow.refresh_sources()
		self.close()

	def open_tutorial(self):
		tutorialText = ""
		with open(addSrcInstPath, "r") as file:
			tutorialText = file.read()
		self.window = InstructionUI(self,tutorialText)
		self.window.show()

	#assumes all number columns have already been verified
	def package_source_form(self):
		dictL = {}
		for sourceColumn in SourceFileColumns:
			inputField = self.findChild(QLineEdit, sourceColumn.value)
			if not sourceColumn in dictL.keys():
				if sourceColumn.value == SourceFileColumns.sourceName.value:
					dictL[sourceColumn.value] = inputField.text()
				else:
					dictL[sourceColumn.value] = str(inputField.text())

		dictL[ExtraSourceFileColumns.typeName.value] = self.ui.typeDdl.currentText()
		dynamicCols = {}
		for dynamicColInd in range(self.ui.dynamicIndexVL.count()):
			dynamicCol = self.ui.dynamicIndexVL.itemAt(dynamicColInd).widget()
			dynamicCols[dynamicCol.objectName()] = dynamicCol.text()
		
		dictL[ExtraSourceFileColumns.typeCols.value] = dynamicCols
		return dictL

	#Add source
	def save_source_clicked(self):
		for sourceColumn in RequiredSourceFileColumns:
			inputField = self.findChild(QLineEdit, sourceColumn.value)
			if inputField:
				if inputField.text() == "":
					self.ui.actionLabel.setText("REQUIRED COLUMN " + inputField.objectName() + " NEEDS NON-EMPTY INPUT")
					return False
		for dynamicColInd in range(self.ui.dynamicIndexVL.count()):
			dynamicCol = self.ui.dynamicIndexVL.itemAt(dynamicColInd).widget()
			if dynamicCol.text() == "":
				self.ui.actionLabel.setText("REQUIRED COLUMN " + dynamicCol.objectName() + " NEEDS NON-EMPTY INPUT")
				return False
		
		#all columns besides sourceName should be a number(index).
		for sourceColumn in SourceFileColumns:
			inputField = self.findChild(QLineEdit, sourceColumn.value)
			if inputField:
				if inputField.text() != "" and sourceColumn.value != SourceFileColumns.sourceName.value:
					try:
						converted = int(inputField.text())
						if converted < 0:
							self.ui.actionLabel.setPlainText("INPUT COLUMN " + inputField.objectName() + " HAS INVALID NUMBER")
							return False

					except ValueError:
						self.ui.actionLabel.setText("INPUT COLUMN " + inputField.objectName() + " NEEDS A NUMBER")
						return False

		for dynamicColInd in range(self.ui.dynamicIndexVL.count()):
			dynamicCol = self.ui.dynamicIndexVL.itemAt(dynamicColInd).widget()
			try:
				converted = int(dynamicCol.text())
				if converted < 0:
					self.ui.actionLabel.setText("INPUT COLUMN " + dynamicCol.objectName() + " HAS INVALID NUMBER")
					return False

			except ValueError:
				self.ui.actionLabel.setText("INPUT COLUMN " + dynamicCol.objectName() + " NEEDS A NUMBER")
				return False
	
		formData = self.package_source_form()

		for sourceColumn in SourceFileColumns:			
			if sourceColumn.value != SourceFileColumns.sourceName.value and sourceColumn.value != SourceFileColumns.skipRows.value:
				for sourceColumnInner in SourceFileColumns:
					if sourceColumnInner.value != SourceFileColumns.sourceName.value and sourceColumnInner.value != SourceFileColumns.skipRows.value and sourceColumnInner.value != sourceColumn.value:	
						if formData[sourceColumn.value] == formData[sourceColumnInner.value] and formData[sourceColumn.value] != "":
							self.ui.actionLabel.setText("DUPLICATE COLUMN INDICES ASSIGNED")
							return False
	

		ret = addSourceToFile(formData)
		if ret:
			self.return_to_main_window()
			return True
		else:
			self.mainWindow.ui.actionLabel.setPlainText("Source could not be added")
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

		for rCol in RequiredSettingsFileColumns:
			el = self.findChild(QLabel, rCol.value + "Label")
			el.setStyleSheet('color: red;')

	def show_settings(self):
		settings = buildSettingsDataFromFile()
		cols = settings.keys()
		for column in cols:
			val = settings[column]
			inputField = self.findChild(QLineEdit, column)
			if inputField:
				inputField.setText(str(val))
						
	def return_to_main_window(self):
		self.close()

	def open_tutorial(self):
		tutorialText = ""
		with open(addSetInstPath, "r") as file:
			tutorialText = file.read()
		self.window = InstructionUI(self,tutorialText)
		self.window.show()

	#assumes all number columns have already been verified
	def package_setting_form(self):
		dictL = {}
		for setColumn in SettingsFileColumns:
			inputField = self.findChild(QLineEdit, setColumn.value)
			if not setColumn in dictL.keys():
				dictL[setColumn.value] = str(inputField.text())
		return dictL

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
			self.mainWindow.ui.actionLabel.setPlainText("Settings could not be updated.")
			self.return_to_main_window()
			return False

class AddTypeUI(QMainWindow):
	def __init__(self, mainWindow):
		super(AddTypeUI, self).__init__()

		self.mainWindow = mainWindow
		self.ui = TypeUi_AddWindow()
		self.ui.setupUi(self)
		self.ui.pluginImportBtn.clicked.connect(self.plugin_import_clicked)
		self.ui.saveBtn.clicked.connect(self.save_type_clicked)
		self.ui.tutorialBtn.clicked.connect(self.open_tutorial)

		for rCol in RequiredTypeFileColumns:
			el = self.findChild(QLabel, rCol.value + "Label")
			el.setStyleSheet('color: red;')
	
	def plugin_import_clicked(self):
		file = QFileDialog.getOpenFileName(self, "Add Plugin", "/~", "Plugins(*.py)")
		if file[0]:
			self.ui.pluginFile.setText(file[0])

	def show_type_clicked(self, type_name):
		types = buildTypeDataFromFile()
		
		for column in TypeFileColumns:
			if column != TypeFileColumns.annotation:
				colName = column.value
				val = types[type_name][colName]
				inputField = self.findChild(QLineEdit, colName)
				inputField.setText(str(val))
		
		txt = types[type_name][TypeFileColumns.annotation.value]
		annotField = self.findChild(QPlainTextEdit, TypeFileColumns.annotation.value)
		annotField.setPlainText(str(txt))
						
	def return_to_main_window(self):
		self.mainWindow.refresh_types()
		self.close()

	def open_tutorial(self):
		tutorialText = ""
		with open(addTypeInstPath, "r") as file:
			tutorialText = file.read()
		self.window = InstructionUI(self,tutorialText)
		self.window.show()

	#assumes all number columns have already been verified
	def package_type_form(self):
		dictL = {}
		for typeColumn in TypeFileColumns:
			if typeColumn != TypeFileColumns.annotation:
				inputField = self.findChild(QLineEdit, typeColumn.value)
				if not typeColumn in dictL.keys():
					dictL[typeColumn.value] = str(inputField.text())
		
		annotField = self.findChild(QPlainTextEdit, TypeFileColumns.annotation.value)
		dictL[TypeFileColumns.annotation.value] = str(annotField.toPlainText())
		return dictL

	def confirm_change_columns_for_type(self):
		choice = QMessageBox.warning(self, 'Confirmation', "Saving this change will cause the column list for this type to be different. If you added columns, these columns indices will need to be specified by the sources that use these types. Proceed with save?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		return choice

	def clean_type_info_for_sources(self):
		sources = buildSourceDataFromFile()
		types = buildTypeDataFromFile()
		for sourcek in sources.keys():
			sourceInfo = sources[sourcek]
			typeName = sourceInfo[ExtraSourceFileColumns.typeName.value]
			typeCols = dict(sourceInfo[ExtraSourceFileColumns.typeCols.value])

			typeInfo = types[typeName]
			realCols = typeInfo[TypeFileColumns.colList.value]
			#make sure all real cols from type file are in source that has that type
			for realCol in realCols.split(","):
				if not realCol in typeCols:
					#set an invalid index so the user will be alerted when they try to use this
					sourceInfo[ExtraSourceFileColumns.typeCols.value][realCol] = "-1"
			#make sure all cols in source are real cols from type file
			for col in typeCols:
				if not col in realCols.split(","):
					sourceInfo[ExtraSourceFileColumns.typeCols.value].pop(col)

			addSourceToFile(sourceInfo)


	def save_type_clicked(self):
		
		for setColumn in RequiredTypeFileColumns:
			inputField = self.findChild(QLineEdit, setColumn.value)
			if inputField:
				if inputField.text() == "":
					self.ui.actionLabel.setText("REQUIRED COLUMN " + inputField.objectName() + " NEEDS NON-EMPTY INPUT")
					return False

		formData = self.package_type_form()
		types = buildTypeDataFromFile()
		typeName = formData[TypeFileColumns.typeName.value]
		afterColList = formData[TypeFileColumns.colList.value]

		#dont want to warn a user when they are adding a new type, since no sources will be affected by colList change yet.
		#dont want to warn a user if they are trying to edit the empty type, since it will fail regardless.
		if typeName in types.keys() and types[typeName][TypeFileColumns.colList.value] != afterColList and typeName != emptyTypeName:
			choice = self.confirm_change_columns_for_type()
			if choice == QMessageBox.Yes:
				ret = addTypeToFile(formData)
				if ret:
					self.clean_type_info_for_sources()
					self.return_to_main_window()
					return True
				else:
					self.mainWindow.ui.actionLabel.setPlainText("Type could not be updated.")
					self.return_to_main_window()
					return False
		else:
			ret = addTypeToFile(formData) #if this is the emptyType/infoType this will fail so no need to prevent explicitly
			if ret:
				self.return_to_main_window()
				return True
			else:
				self.mainWindow.ui.actionLabel.setPlainText("Type could not be updated.")
				self.return_to_main_window()
				return False

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainUI()
	window.show()
	sys.exit(app.exec_())
