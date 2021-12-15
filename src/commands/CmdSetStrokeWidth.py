from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QWidget
from commands.CommandInterface import CommandInterface

from PyQt5.QtWidgets import QWidget, QSlider, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout
from PyQt5.QtCore import Qt



class CmdSetStrokeWidth(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = False
    def execute(self, *args):
        if (type(args[0]) == float):    #if width argument #what is this behavior?
            self.view.grafikView.setStrokeWidth(args[0])
        else: #if no parameter -> strokeWidthPicker
            strokeWidthPicker = StrokeWidthPicker(self.view)
            strokeWidthPicker.exec()
            
            

        print("CmdSetStrokeWidth executed")      
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool

    


class StrokeWidthPicker(QDialog):
    def __init__(self, parent = None):
        print("init")
                                #VIEW?
        super(StrokeWidthPicker, self).__init__(parent)
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        sld = QSlider(Qt.Horizontal, self)
        sld.setRange(0, 100)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setPageStep(5)

        sld.valueChanged.connect(self.updateLabel)

        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label.setMinimumWidth(80)

        hbox.addWidget(sld)
        hbox.addSpacing(15)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.setGeometry(0,0,500,100)
        self.setWindowTitle('QSlider')

        self.show()

    def updateLabel(self, value):

        self.label.setText(str(value))
        
