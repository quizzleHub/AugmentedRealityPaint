from commands.CommandInterface import CommandInterface
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets


class CmdSetStrokeWidth(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = False
        self.strokePatternLookUp = {
            0:Qt.SolidLine,
            1:Qt.DashLine,
            2:Qt.DotLine,
            3:Qt.DashDotLine,
            4:Qt.DashDotDotLine,
        }
        self.brushStyleLookUp = {
            0:Qt.SolidPattern,
            1:Qt.Dense1Pattern,
            2:Qt.Dense2Pattern,
            3:Qt.Dense3Pattern,
            4:Qt.Dense4Pattern,
            5:Qt.Dense5Pattern,
            6:Qt.Dense6Pattern,
            7:Qt.Dense7Pattern,
            8:Qt.HorPattern,
            9:Qt.VerPattern,
            10:Qt.CrossPattern,
            11:Qt.BDiagPattern,
            12:Qt.FDiagPattern,
            13:Qt.DiagCrossPattern
        }
        self.penCapStyleLookUp = {
            0:Qt.SquareCap,
            1:Qt.FlatCap,
            2:Qt.RoundCap
        }

    def execute(self, *args):
        if (type(args[0]) == float):    #if width argument #what is this behavior?
            self.view.graphicsView.setStrokeWidth(args[0])
        else: #if no parameter -> strokeWidthPicker
            #strokeWidthPicker = StrokeWidthPicker(self.view)
            #strokeWidthPicker.exec()
            self.penPickerDialog = QtWidgets.QDialog()
            self.penPickerUi = Ui_Dialog()
            self.penPickerUi.setupUi(self.penPickerDialog)
            self.penPickerUi.btnApplySettings.clicked.connect(self.getSelectedPenProperties)
            self.getCurrentPenProperties()
            self.penPickerDialog.exec()

        if args[1] == self.view.getbtnThick():
            self.view.getbtnMedium().setChecked(False)
            self.view.getbtnThin().setChecked(False)

        if args[1] == self.view.getbtnMedium():
            self.view.getbtnThick().setChecked(False)
            self.view.getbtnThin().setChecked(False)

        if args[1] == self.view.getbtnThin():
            self.view.getbtnThick().setChecked(False)
            self.view.getbtnMedium().setChecked(False)

        if args[1] == self.view.getbtnStrokeWidthPicker():
            self.view.getbtnThick().setChecked(False)
            self.view.getbtnMedium().setChecked(False)
            self.view.getbtnThin().setChecked(False)

    def redo(self):
        pass

    def undo(self):
        pass

    def isUndoable(self):
        return self.isUndoableBool

    def getSelectedPenProperties(self):
        self.strokeWidth = self.penPickerUi.sldStrokeWidth.value()
        self.strokePattern = self.strokePatternLookUp[self.penPickerUi.cmbBoxStrokePattern.currentIndex()]
        self.brushStyle = self.brushStyleLookUp[self.penPickerUi.cmbBoxBrushStyle.currentIndex()]
        self.penCapStyle = self.penCapStyleLookUp[self.penPickerUi.cmbBoxPenCapStyle.currentIndex()]
        self.setPenProperties()
  
    def setPenProperties(self):
        self.view.graphicsView.setStrokeWidth(self.strokeWidth)
        self.view.graphicsView.setStrokePattern(self.strokePattern)
        self.view.graphicsView.setBrushStyle(self.brushStyle)
        self.view.graphicsView.setPenCapStyle(self.penCapStyle)
        self.penPickerDialog.close()

    def getCurrentPenProperties(self):
        self.penPickerUi.sldStrokeWidth.setValue(self.view.graphicsView.getStrokeWidth())
        #get key by value -> rip
        strokePatternIndex = list(self.strokePatternLookUp.keys())[list(self.strokePatternLookUp.values()).index(self.view.graphicsView.getStrokePattern())]
        self.penPickerUi.cmbBoxStrokePattern.setCurrentIndex(strokePatternIndex)

        brushStyleIndex = list(self.brushStyleLookUp.keys())[list(self.brushStyleLookUp.values()).index(self.view.graphicsView.getBrushStyle())]
        self.penPickerUi.cmbBoxBrushStyle.setCurrentIndex(brushStyleIndex)

        penCapStyleIndex = list(self.penCapStyleLookUp.keys())[list(self.penCapStyleLookUp.values()).index(self.view.graphicsView.getPenCapStyle())]
        self.penPickerUi.cmbBoxPenCapStyle.setCurrentIndex(penCapStyleIndex)
    
    
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
        self.lblStrokePattern.setText(_translate("Dialog", "Stroke pattern"))
        self.lblPenCapStyle.setText(_translate("Dialog", "Pen cap style"))
        self.cmbBoxPenCapStyle.setItemText(0, _translate("Dialog", "Square cap"))
        self.cmbBoxPenCapStyle.setItemText(1, _translate("Dialog", "Flat cap"))
        self.cmbBoxPenCapStyle.setItemText(2, _translate("Dialog", "Round cap"))
        self.btnApplySettings.setText(_translate("Dialog", "Apply settings"))