import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.filename = ""
		self.count = 1
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Text Editor")
		self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
		self.initActions()
		self.initMenuBar()
		self.initActionsToolBar()
		self.initFormatsToolBar()
		self.statusBar()
		self.winmain()


	def initActionsToolBar(self):
		self.actionsToolBar = self.addToolBar("Actions Toolbar")
		self.actionsToolBar.setStatusTip("Actions Toolbar")
		self.actionsToolBar.addAction(self.newtxtaction)
		self.actionsToolBar.addAction(self.newhtmlaction)
		self.actionsToolBar.addAction(self.openaction)
		self.actionsToolBar.addAction(self.saveaction)
		self.actionsToolBar.addSeparator()
		self.actionsToolBar.addAction(self.previewaction)
		self.actionsToolBar.addAction(self.printaction)
		self.actionsToolBar.addSeparator()
		self.actionsToolBar.addAction(self.cutaction)
		self.actionsToolBar.addAction(self.copyaction)
		self.actionsToolBar.addAction(self.pasteaction)
		self.actionsToolBar.addSeparator()
		self.actionsToolBar.addAction(self.imageaction)
		self.actionsToolBar.addSeparator()
		self.actionsToolBar.addAction(self.bulletaction)
		self.actionsToolBar.addAction(self.numberedaction)
		self.actionsToolBar.addAction(self.zoominaction)
		self.actionsToolBar.addAction(self.zoomoutaction)
		self.actionsToolBar.addSeparator()
		self.actionsToolBar.addAction(self.undoaction)
		self.actionsToolBar.addAction(self.redoaction)
		self.actionsToolBar.addSeparator()
		self.actionsToolBar.addAction(self.qaction)
		self.actionsToolBar.addSeparator()
		self.addToolBarBreak()

	def initFormatsToolBar(self):
		self.formatsToolBar = self.addToolBar("Formats Toolbar")
		self.formatsToolBar.setStatusTip("Formats Toolbar")
		self.formatsToolBar.addAction(self.boldaction)
		self.formatsToolBar.addAction(self.italicaction)
		self.formatsToolBar.addAction(self.underlaction)
		self.formatsToolBar.addSeparator()
		self.formatsToolBar.addAction(self.superaction)
		self.formatsToolBar.addAction(self.subaction)
		self.formatsToolBar.addSeparator()


	def initMenuBar(self):
		mainMenu = self.menuBar()
		mainMenu.setStatusTip("MenuBar")
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.setStatusTip("File Menu")
		newMenu = fileMenu.addMenu('&New')
		newMenu.addAction(self.newtxtaction)
		newMenu.addAction(self.newhtmlaction)
		fileMenu.addAction(self.openaction)
		fileMenu.addAction(self.saveaction)
		fileMenu.addSeparator()
		fileMenu.addAction(self.previewaction)
		fileMenu.addAction(self.printaction)
		fileMenu.addSeparator()
		fileMenu.addAction(self.qaction)
		fileMenu.addSeparator()

		editMenu = mainMenu.addMenu('&Edit')
		editMenu.addAction(self.undoaction)
		editMenu.addAction(self.redoaction)
		editMenu.addSeparator()
		editMenu.addAction(self.cutaction)
		editMenu.addAction(self.copyaction)
		editMenu.addAction(self.pasteaction)
		editMenu.addSeparator()
		fontMenu = editMenu.addMenu('&Font')
		fontMenu.addAction(self.boldaction)
		fontMenu.addAction(self.italicaction)
		fontMenu.addAction(self.underlaction)
		fontMenu.addSeparator()
		fontMenu.addAction(self.superaction)
		fontMenu.addAction(self.subaction)
		insertMenu = editMenu.addMenu('&Insert')
		insertMenu.addAction(self.imageaction)
		insertMenu.addSeparator()
		insertMenu.addAction(self.bulletaction)
		insertMenu.addAction(self.numberedaction)
		insertMenu.addSeparator()
		editMenu.addSeparator()


		viewMenu = mainMenu.addMenu('&View')
		viewMenu.addAction(self.zoominaction)
		viewMenu.addAction(self.zoomoutaction)
		viewMenu.addSeparator()

		settingsMenu = mainMenu.addMenu('&Settings')
		settingsMenu.addMenu('&Appearance')

	def initActions(self):
		self.newtxtaction = QtGui.QAction("&Text", self)
		self.newtxtaction.setShortcut("Ctrl+N")
		self.newtxtaction.setStatusTip("New TXT File")
		QtCore.QObject.connect(self.newtxtaction, QtCore.SIGNAL('triggered()'), self.file_newtxt)

		self.newhtmlaction = QtGui.QAction(QtGui.QIcon('icons/new.png'), "&HTML", self)
		self.newhtmlaction.setShortcut("Ctrl+N")
		self.newhtmlaction.setStatusTip("New HTML File")
		QtCore.QObject.connect(self.newhtmlaction, QtCore.SIGNAL('triggered()'), self.file_newhtml)

		self.openaction = QtGui.QAction(QtGui.QIcon('icons/open.png'), "&Open", self)
		self.openaction.setShortcut("Ctrl+O")
		self.openaction.setStatusTip("Open File")
		QtCore.QObject.connect(self.openaction, QtCore.SIGNAL('triggered()'), self.file_open)

		self.saveaction = QtGui.QAction(QtGui.QIcon('icons/save.png'), "&Save", self)
		self.saveaction.setShortcut("Ctrl+S")
		self.saveaction.setStatusTip("Save File")
		QtCore.QObject.connect(self.saveaction, QtCore.SIGNAL('triggered()'), self.file_save)

		self.qaction = QtGui.QAction(QtGui.QIcon('icons/quit.png'), "&Quit", self)
		self.qaction.setShortcut("Ctrl+Q")
		self.qaction.setStatusTip('Quit Application')
		QtCore.QObject.connect(self.qaction, QtCore.SIGNAL('triggered()'), self.close_application)

		self.printaction = QtGui.QAction(QtGui.QIcon("icons/print.png"), "&Print", self)
		self.printaction.setStatusTip("Print document")
		self.printaction.setShortcut("Ctrl+P")
		QtCore.QObject.connect(self.printaction, QtCore.SIGNAL('triggered()'), self.print)

		self.previewaction = QtGui.QAction(QtGui.QIcon("icons/preview.png"), "&Print Preview", self)
		self.previewaction.setStatusTip("Preview page before printing")
		self.previewaction.setShortcut("Ctrl+Shift+P")
		QtCore.QObject.connect(self.previewaction, QtCore.SIGNAL('triggered()'), self.preview)

		self.zoominaction = QtGui.QAction(QtGui.QIcon("icons/zoomin.png"), "&Zoom In", self)
		self.zoominaction.setStatusTip("Zoom In")
		self.zoominaction.setShortcut("Ctrl+1")
		QtCore.QObject.connect(self.zoominaction, QtCore.SIGNAL('triggered()'), self.zoomin)

		self.zoomoutaction = QtGui.QAction(QtGui.QIcon("icons/zoomout.png"), "&Zoom Out", self)
		self.zoomoutaction.setStatusTip("Zoom Out")
		self.zoomoutaction.setShortcut("Ctrl+2")
		QtCore.QObject.connect(self.zoomoutaction, QtCore.SIGNAL('triggered()'), self.zoomout)

		self.cutaction = QtGui.QAction(QtGui.QIcon("icons/cut.png"), "&Cut", self)
		self.cutaction.setStatusTip("Delete and copy text to clipboard")
		self.cutaction.setShortcut("Ctrl+X")
		QtCore.QObject.connect(self.cutaction, QtCore.SIGNAL('triggered()'), self.cut)

		self.copyaction = QtGui.QAction(QtGui.QIcon("icons/copy.png"), "&Copy", self)
		self.copyaction.setStatusTip("Copy text to clipboard")
		self.copyaction.setShortcut("Ctrl+C")
		QtCore.QObject.connect(self.copyaction, QtCore.SIGNAL('triggered()'), self.copy)

		self.pasteaction = QtGui.QAction(QtGui.QIcon("icons/paste.png"), "&Paste", self)
		self.pasteaction.setStatusTip("Paste text to document")
		self.pasteaction.setShortcut("Ctrl+V")
		QtCore.QObject.connect(self.pasteaction, QtCore.SIGNAL('triggered()'), self.paste)

		self.undoaction = QtGui.QAction(QtGui.QIcon("icons/undo.png"), "&Undo", self)
		self.undoaction.setStatusTip("Undo last action")
		self.undoaction.setShortcut("Ctrl+Z")
		QtCore.QObject.connect(self.undoaction, QtCore.SIGNAL('triggered()'), self.undo)

		self.redoaction = QtGui.QAction(QtGui.QIcon("icons/redo.png"), "&Redo", self)
		self.redoaction.setStatusTip("Redo last undone thing")
		self.redoaction.setShortcut("Ctrl+Y")
		QtCore.QObject.connect(self.redoaction, QtCore.SIGNAL('triggered()'), self.redo)

		self.bulletaction = QtGui.QAction(QtGui.QIcon("icons/bulletlist.png"), "&Bullet List", self)
		self.bulletaction.setStatusTip("Insert bullet list")
		self.bulletaction.setShortcut("Ctrl+Shift+B")
		QtCore.QObject.connect(self.bulletaction, QtCore.SIGNAL('triggered()'), self.bulletlist)

		self.numberedaction = QtGui.QAction(QtGui.QIcon("icons/numberedlist.png"), "&Numbered List", self)
		self.numberedaction.setStatusTip("Insert numbered list")
		self.numberedaction.setShortcut("Ctrl+Shift+L")
		QtCore.QObject.connect(self.numberedaction, QtCore.SIGNAL('triggered()'), self.numberlist)

		self.boldaction = QtGui.QAction(QtGui.QIcon("icons/bold.png"), "&Bold", self)
		self.boldaction.setStatusTip("Trigger font bold on/off")
		self.boldaction.setShortcut("Ctrl+B")
		QtCore.QObject.connect(self.boldaction, QtCore.SIGNAL('triggered()'), self.bold)

		self.italicaction = QtGui.QAction(QtGui.QIcon("icons/italic.png"), "&Italic", self)
		self.italicaction.setStatusTip("Trigger font italicize on/off")
		self.italicaction.setShortcut("Ctrl+I")
		QtCore.QObject.connect(self.italicaction, QtCore.SIGNAL('triggered()'), self.italic)

		self.underlaction = QtGui.QAction(QtGui.QIcon("icons/underline.png"), "&Underline", self)
		self.underlaction.setStatusTip("Trigger font underline on/off")
		self.underlaction.setShortcut("Ctrl+U")
		QtCore.QObject.connect(self.underlaction, QtCore.SIGNAL('triggered()'), self.underline)

		self.superaction = QtGui.QAction(QtGui.QIcon("icons/superscript.png"), "&Superscript", self)
		self.superaction.setStatusTip("Trigger font superscript on/off")
		self.superaction.setShortcut("Ctrl+Shift+=")
		QtCore.QObject.connect(self.superaction, QtCore.SIGNAL('triggered()'), self.superscript)

		self.subaction = QtGui.QAction(QtGui.QIcon("icons/subscript.png"), "&Subscript", self)
		self.subaction.setStatusTip("Trigger font subscript on/off")
		self.subaction.setShortcut("Ctrl+Shift+-")
		QtCore.QObject.connect(self.subaction, QtCore.SIGNAL('triggered()'), self.subscript)

		self.imageaction = QtGui.QAction(QtGui.QIcon("icons/image.png"), "Insert image", self)
		self.imageaction.setStatusTip("Insert image")
		self.imageaction.setShortcut("Ctrl+Shift+I")
		QtCore.QObject.connect(self.imageaction, QtCore.SIGNAL('triggered()'), self.insertimage)

	def initTab(self):
		self.tab_widget = QtGui.QTabWidget(self)
		self.tab_widget.setTabsClosable(True)
		self.tab_widget.setMovable(True)
		self.tab_widget.tabCloseRequested.connect(self.closetab)
		font = QtGui.QFont("Times", 10)
		self.fontsize = 10
		self.initialfontsize = 10
		self.tab_widget.setFont(font)

	def winmain(self):
		self.initTab()

		self.setCentralWidget(self.tab_widget)
		self.showapp()

	def showapp(self):
		self.showMaximized()

	def zoomin(self):
		self.fontsize += 2
		font = QtGui.QFont("Times", self.fontsize)
		self.tab_widget.currentWidget().setFont(font)

	def zoomout(self):
		self.fontsize -= 2
		font = QtGui.QFont("Times", self.fontsize)
		self.tab_widget.currentWidget().setFont(font)

	def cut(self):
		self.tab_widget.currentWidget().cut()

	def copy(self):
		self.tab_widget.currentWidget().copy()

	def paste(self):
		self.tab_widget.currentWidget().paste()

	def undo(self):
		self.tab_widget.currentWidget().undo()

	def redo(self):
		self.tab_widget.currentWidget().redo()

	def bulletlist(self):
		cursor = self.tab_widget.currentWidget().textCursor()

	# Insert bulleted list
		cursor.insertList(QtGui.QTextListFormat.ListDisc)

	def numberlist(self):
		cursor = self.tab_widget.currentWidget().textCursor()

		# Insert list with numbers
		cursor.insertList(QtGui.QTextListFormat.ListDecimal)

	def bold(self):
		if self.tab_widget.currentWidget().fontWeight() == QtGui.QFont.Bold:

			self.tab_widget.currentWidget().setFontWeight(QtGui.QFont.Normal)

		else:

			self.tab_widget.currentWidget().setFontWeight(QtGui.QFont.Bold)

	def italic(self):
		state = self.tab_widget.currentWidget().fontItalic()

		self.tab_widget.currentWidget().setFontItalic(not state)

	def underline(self):
		state = self.tab_widget.currentWidget().fontUnderline()

		self.tab_widget.currentWidget().setFontUnderline(not state)

	def superscript(self):
		# Grab the current format
		fmt = self.tab_widget.currentWidget().currentCharFormat()

		# And get the vertical alignment property
		align = fmt.verticalAlignment()

		# Toggle the state
		if align == QtGui.QTextCharFormat.AlignNormal:

			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)

		else:

			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

		# Set the new format
		self.tab_widget.currentWidget().setCurrentCharFormat(fmt)

	def subscript(self):
		# Grab the current format
		fmt = self.tab_widget.currentWidget().currentCharFormat()

		# And get the vertical alignment property
		align = fmt.verticalAlignment()

		# Toggle the state
		if align == QtGui.QTextCharFormat.AlignNormal:

			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)

		else:

			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

		# Set the new format
		self.tab_widget.currentWidget().setCurrentCharFormat(fmt)

	def insertimage(self):
		# Get image file name
		filename = QtGui.QFileDialog.getOpenFileName(self, 'Insert image', ".", "Images (*.png *.xpm *.jpg *.bmp *.gif)")

		# Create image object
		image = QtGui.QImage(filename)

		# Error if unloadable
		if image.isNull():

			popup = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
									  "Image load error",
									  "Could not load image file!",
									  QtGui.QMessageBox.Ok,
									  self)
			popup.show()

		else:

			cursor = self.tab_widget.currentWidget().textCursor()

			cursor.insertImage(image,filename)

	def closetab(self, currentindex):
		self.tab_widget.removeTab(currentindex)

	def file_newtxt(self):
		text_widget = QtGui.QPlainTextEdit(self.tab_widget)
		self.tab_widget.addTab(text_widget, "untitled" + str(self.count) + ".txt")
		self.count += 1

	def file_newhtml(self):
		text_widget = QtGui.QTextEdit(self.tab_widget)
		text_widget.setText('')
		self.tab_widget.addTab(text_widget, "untitled" + str(self.count) + ".html")
		self.count += 1

	def file_open(self):
		name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
		file = open(name, 'r')
		with open(name, 'r') as f:
			filedata = f.read()
			text_widget = QtGui.QTextEdit(self.tab_widget)
			text_widget.setText(filedata)
			reverse = name[::-1]
			index = reverse.find("/")
			shortreverse = reverse[:index]
			filename = shortreverse[::-1]
			self.tab_widget.addTab(text_widget, filename)

		with file:
			text = file.read()
			self.textEdit.setText(text)

	def file_save(self):
		name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

		if not name.endswith(".html"):
			name += ".html"
		file = open(name, 'w')
		file.write(self.tab_widget.currentWidget().toHtml())

		file.close()

		index = self.tab_widget.currentIndex()
		reverse = name[::-1]
		i = reverse.find("/")
		shortreverse = reverse[:i]
		filename = shortreverse[::-1]
		self.tab_widget.setTabText(index, filename)


	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Quit', "Exit Application", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			print("Closing Application!")
			sys.exit()
		else:
			pass

	def preview(self):
		# Open preview dialog
		preview = QtGui.QPrintPreviewDialog()

		# If a print is requested, open print dialog
		preview.paintRequested.connect(lambda p: self.tab_widget.currentWidget().print_(p))

		preview.exec_()

	def print(self):

		# Open printing dialog
		dialog = QtGui.QPrintDialog()

		if dialog.exec_() == QtGui.QDialog.Accepted:
			self.tab_widget.currentWidget().document().print_(dialog.printer())

def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
