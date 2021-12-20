from commands.CommandInterface import CommandInterface
from PyQt5 import QtCore, QtWidgets
import codecs
from pathlib import Path

#https://github.com/smoqadam/pyqt-md-reader/blob/master/main.py

class CmdHelp(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = False
        self.htmlContent = codecs.open(Path(__file__).with_name('Help.html'), 'r').read()
        
    def execute(self, *args):
        self.helpDialog = QtWidgets.QDialog()
        self.helpDialogUi = Ui_Help()
        self.helpDialogUi.setupUi(self.helpDialog)
        self.helpDialogUi.buttonBox.clicked.connect(self.quitHelp)
        self.helpDialogUi.textEdit.textCursor().insertHtml(self.htmlContent)
        self.helpDialog.exec()

    def redo(self):
        pass

    def undo(self):
        pass

    def isUndoable(self):
        return self.isUndoableBool

    def quitHelp(self):
        self.helpDialog.close()


class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(768, 548)
        Help.setWindowTitle("Help")
        self.verticalLayout = QtWidgets.QVBoxLayout(Help)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(Help)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.verticalLayout.addWidget(self.textEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(Help)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        