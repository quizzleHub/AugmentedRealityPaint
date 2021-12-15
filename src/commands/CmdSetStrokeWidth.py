from typing import Match
from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5 import QtWidgets
from commands.CommandInterface import CommandInterface

from PyQt5.QtWidgets import QWidget, QSlider, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets



class CmdSetStrokeWidth(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = False
        self.strokePatternLookUp = {
            0:1,
            1:2,
            2:3,
            3:4,
            4:5,
        }
        self.brushStyleLookUp = {
            0:1,
            1:2,
            2:3,
            3:4,
            4:5,
            5:6

        }

    def execute(self, *args):
        if (type(args[0]) == float):    #if width argument #what is this behavior?
            self.view.grafikView.setStrokeWidth(args[0])
        else: #if no parameter -> strokeWidthPicker
            #strokeWidthPicker = StrokeWidthPicker(self.view)
            #strokeWidthPicker.exec()
            self.penPickerDialog = QtWidgets.QDialog()
            self.penPickerUi = Ui_Dialog()
            self.penPickerUi.setupUi(self.penPickerDialog)
            self.penPickerUi.btnApplySettings.clicked.connect(self.getPenProperties)
            self.penPickerDialog.exec()
            
            
        print("CmdSetStrokeWidth executed")      
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool
    def getPenProperties(self):
        self.strokeWidth = self.penPickerUi.sldStrokeWidth.value()
        self.strokePattern = self.penPickerUi.cmbBoxStrokePattern.currentIndex()
        self.brushStyle = self.penPickerUi.cmbBoxBrushStyle.currentIndex()
        self.penCapStyle = self.penPickerUi.cmbBoxPenCapStyle.currentIndex()
        #map pencapstyle to correct hex val
        if(self.penCapStyle == 0):
            self.penCapStyle = 0x10
        elif(self.penCapStyle == 1):
            self.penCapStyle = 0x00
        else:
            self.penCapStyle = 0x20
        self.setPenProperties()

        
        
    def setPenProperties(self):
        self.view.grafikView.setStrokeWidth(self.strokeWidth)
        self.view.grafikView.setStrokePattern(self.strokePattern+1) #offset noPattern
        self.view.grafikView.setBrushStyle(self.brushStyle+1)   #offset noBrush
        self.view.grafikView.setPenCapStyle(self.penCapStyle)
        self.penPickerDialog.close()



    



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(504, 194)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblStrokeWidth = QtWidgets.QLabel(Dialog)
        self.lblStrokeWidth.setObjectName("lblStrokeWidth")
        self.gridLayout.addWidget(self.lblStrokeWidth, 0, 0, 1, 1)
        self.lblBrushStyle = QtWidgets.QLabel(Dialog)
        self.lblBrushStyle.setObjectName("lblBrushStyle")
        self.gridLayout.addWidget(self.lblBrushStyle, 2, 0, 1, 1)
        self.cmbBoxStrokePattern = QtWidgets.QComboBox(Dialog)
        self.cmbBoxStrokePattern.setMaxVisibleItems(6)
        self.cmbBoxStrokePattern.setMaxCount(6)
        self.cmbBoxStrokePattern.setObjectName("cmbBoxStrokePattern")
        self.cmbBoxStrokePattern.addItem("")
        self.cmbBoxStrokePattern.addItem("")
        self.cmbBoxStrokePattern.addItem("")
        self.cmbBoxStrokePattern.addItem("")
        self.cmbBoxStrokePattern.addItem("")
        self.gridLayout.addWidget(self.cmbBoxStrokePattern, 1, 1, 1, 1)
        self.sldStrokeWidth = QtWidgets.QSlider(Dialog)
        self.sldStrokeWidth.setMinimum(1)
        self.sldStrokeWidth.setMaximum(40)
        self.sldStrokeWidth.setSliderPosition(3)
        self.sldStrokeWidth.setTracking(True)
        self.sldStrokeWidth.setOrientation(QtCore.Qt.Horizontal)
        self.sldStrokeWidth.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sldStrokeWidth.setTickInterval(1)
        self.sldStrokeWidth.setObjectName("sldStrokeWidth")
        self.gridLayout.addWidget(self.sldStrokeWidth, 0, 1, 1, 1)
        self.cmbBoxBrushStyle = QtWidgets.QComboBox(Dialog)
        self.cmbBoxBrushStyle.setObjectName("cmbBoxBrushStyle")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.cmbBoxBrushStyle.addItem("")
        self.gridLayout.addWidget(self.cmbBoxBrushStyle, 2, 1, 1, 1)
        self.lblStrokePattern = QtWidgets.QLabel(Dialog)
        self.lblStrokePattern.setObjectName("lblStrokePattern")
        self.gridLayout.addWidget(self.lblStrokePattern, 1, 0, 1, 1)
        self.lblPenCapStyle = QtWidgets.QLabel(Dialog)
        self.lblPenCapStyle.setObjectName("lblPenCapStyle")
        self.gridLayout.addWidget(self.lblPenCapStyle, 3, 0, 1, 1)
        self.cmbBoxPenCapStyle = QtWidgets.QComboBox(Dialog)
        self.cmbBoxPenCapStyle.setObjectName("cmbBoxPenCapStyle")
        self.cmbBoxPenCapStyle.addItem("")
        self.cmbBoxPenCapStyle.addItem("")
        self.cmbBoxPenCapStyle.addItem("")
        self.gridLayout.addWidget(self.cmbBoxPenCapStyle, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.btnApplySettings = QtWidgets.QPushButton(Dialog)
        self.btnApplySettings.setObjectName("btnApplySettings")
        self.verticalLayout.addWidget(self.btnApplySettings)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pen picker"))
        self.lblStrokeWidth.setText(_translate("Dialog", "Stroke width:"))
        self.lblBrushStyle.setText(_translate("Dialog", "Brush style"))
        self.cmbBoxStrokePattern.setItemText(0, _translate("Dialog", "Solid line"))
        self.cmbBoxStrokePattern.setItemText(1, _translate("Dialog", "Dash line"))
        self.cmbBoxStrokePattern.setItemText(2, _translate("Dialog", "Dot line"))
        self.cmbBoxStrokePattern.setItemText(3, _translate("Dialog", "Dash dot line"))
        self.cmbBoxStrokePattern.setItemText(4, _translate("Dialog", "Dash dot dot line"))
        self.cmbBoxBrushStyle.setItemText(0, _translate("Dialog", "Solid pattern"))
        self.cmbBoxBrushStyle.setItemText(1, _translate("Dialog", "Dense 1 pattern"))
        self.cmbBoxBrushStyle.setItemText(2, _translate("Dialog", "Dense 2 pattern"))
        self.cmbBoxBrushStyle.setItemText(3, _translate("Dialog", "Dense 3 pattern"))
        self.cmbBoxBrushStyle.setItemText(4, _translate("Dialog", "Dense 4 pattern"))
        self.cmbBoxBrushStyle.setItemText(5, _translate("Dialog", "Dense 5 pattern"))
        self.cmbBoxBrushStyle.setItemText(6, _translate("Dialog", "Dense 6 pattern"))
        self.cmbBoxBrushStyle.setItemText(7, _translate("Dialog", "Dense 7 pattern"))
        self.cmbBoxBrushStyle.setItemText(8, _translate("Dialog", "Horizontal pattern"))
        self.cmbBoxBrushStyle.setItemText(9, _translate("Dialog", "Vertical pattern"))
        self.cmbBoxBrushStyle.setItemText(10, _translate("Dialog", "Cross pattern"))
        self.cmbBoxBrushStyle.setItemText(11, _translate("Dialog", "B-diagonal pattern"))
        self.cmbBoxBrushStyle.setItemText(12, _translate("Dialog", "F-diagonal pattern"))
        self.cmbBoxBrushStyle.setItemText(13, _translate("Dialog", "Diagonal cross pattern"))
        self.cmbBoxBrushStyle.setItemText(14, _translate("Dialog", "Linear gradient pattern"))
        self.cmbBoxBrushStyle.setItemText(15, _translate("Dialog", "Radial gradient pattern"))
        self.cmbBoxBrushStyle.setItemText(16, _translate("Dialog", "Conical gradient pattern"))
        self.lblStrokePattern.setText(_translate("Dialog", "Stroke pattern"))
        self.lblPenCapStyle.setText(_translate("Dialog", "Pen cap style"))
        self.cmbBoxPenCapStyle.setItemText(0, _translate("Dialog", "Square cap"))
        self.cmbBoxPenCapStyle.setItemText(1, _translate("Dialog", "Flat cap"))
        self.cmbBoxPenCapStyle.setItemText(2, _translate("Dialog", "Round cap"))
        self.btnApplySettings.setText(_translate("Dialog", "Apply settings"))

        #connect
        #self.btnApplySettings.clicked.connect(self.returnVals)




        
