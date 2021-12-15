from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QSize
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QColorDialog
from commands.CmdSetStrokeColor import CmdSetStrokeColor
from commands.CmdSetStrokeWidth import CmdSetStrokeWidth

from commands.CommandInvoker import CommandInvoker
from commands.CmdCalibrateCVCol import CmdCalibrateCVCol
from commands.CmdSafeFigures import CmdSafeFigures
from commands.CmdOpenFigures import CmdOpenFigures



class MainController(QObject):  # windowListener, ActionListener

    def __init__(self, view, cvModelThread, cvModel, graphicsModel):
        super().__init__()
        self.view = view
        self.cvModelThread = cvModelThread
        self.cvModel = cvModel
        self.graphicsModel = graphicsModel
        self.commandInvoker = CommandInvoker()
        

        # get buttons
        self.btnClear_all = self.view.getbtnClear_all()
        self.btnOpen = self.view.getbtnOpen()
        self.btnSave = self.view.getbtnSave()
        self.btnCalibrate = self.view.getbtnCalibrate()
        self.btnHelp = self.view.getbtnHelp()
        self.btnPaint = self.view.getbtnPaint()
        self.btnErase = self.view.getbtnErase()
        self.btnRed = self.view.getbtnRed()
        self.btnBlue = self.view.getbtnBlue()
        self.btnYellow = self.view.getbtnYellow()
        self.btnThick = self.view.getbtnThick()
        self.btnMedium = self.view.getbtnMedium()
        self.btnThin = self.view.getbtnThin()
        self.btnUndo = self.view.getbtnUndo()
        self.btnRedo = self.view.getbtnRedo()
        self.btnColorPicker = self.view.getbtnColorPicker()
        self.btnStrokeWidthPicker = self.view.getbtnStrokeWidthPicker()

        # all commands
        self.cmdCalibrateCVCol = CmdCalibrateCVCol(self.view, self.cvModel)
        self.cmdSafeFigures = CmdSafeFigures(self.view, self.graphicsModel)
        self.cmdOpenFigures = CmdOpenFigures(self.view, self.graphicsModel)
        self.cmdSetStrokeColor = CmdSetStrokeColor(self.view, self.graphicsModel)
        self.cmdSetStrokeWidth = CmdSetStrokeWidth(self.view, self.graphicsModel)
        # etc...

        # set correct window aspectratio for camera
        self.aspectRatio = self.cvModel.aspectRatio
        self.view.resize(self.view.width(), self.view.width() / self.aspectRatio)

    def registerEvents(self):
        # register event to actionPerformed for all buttons
        #self.btnClear_all.triggered.connect(self.actionPerformed)
        self.btnOpen.triggered.connect(self.actionPerformed)
        self.btnSave.triggered.connect(self.actionPerformed)
        self.btnCalibrate.triggered.connect(self.actionPerformed)
        self.btnHelp.triggered.connect(self.actionPerformed)

        #self.btnPaint.triggered.connect(self.actionPerformed)
        #self.btnErase.triggered.connect(self.actionPerformed)

        self.btnBlue.triggered.connect(lambda: self.actionPerformed(QColor(102, 140, 255)))
        self.btnYellow.triggered.connect(lambda: self.actionPerformed(QColor(255,255,128)))
        self.btnRed.triggered.connect(lambda: self.actionPerformed(QColor(255,102,102)))
        self.btnColorPicker.triggered.connect(lambda: self.actionPerformed(QColorDialog.getColor()))
        self.btnThick.triggered.connect(lambda: self.actionPerformed(7.3))
        self.btnMedium.triggered.connect(lambda: self.actionPerformed(4.3))
        self.btnThin.triggered.connect(lambda: self.actionPerformed(1.3))
        #strokewidthpicker
        print("registered events in BtnController")

    def registerCommands(self):
        # register buttons to commands
        self.commandInvoker.addCommand(self.btnOpen, self.cmdOpenFigures)
        self.commandInvoker.addCommand(self.btnSave, self.cmdSafeFigures)
        self.commandInvoker.addCommand(self.btnCalibrate, self.cmdCalibrateCVCol)

        self.commandInvoker.addCommand(self.btnBlue, self.cmdSetStrokeColor)
        self.commandInvoker.addCommand(self.btnYellow, self.cmdSetStrokeColor)
        self.commandInvoker.addCommand(self.btnRed, self.cmdSetStrokeColor)
        self.commandInvoker.addCommand(self.btnColorPicker, self.cmdSetStrokeColor)

        self.commandInvoker.addCommand(self.btnThick, self.cmdSetStrokeWidth)
        self.commandInvoker.addCommand(self.btnMedium, self.cmdSetStrokeWidth)
        self.commandInvoker.addCommand(self.btnThin, self.cmdSetStrokeWidth)
        print("registerd Commands in BtnController")

    def connectSignals(self):
        self.cvModelThread.started.connect(self.cvModel.run)
        self.cvModel.newCamFrame.connect(self.view.grafikView.updateCanvas)
        self.cvModel.newTrackedCoords.connect(self.graphicsModel.addPoint)
        self.cvModel.exitSig.connect(self.cvModelThread.quit)

        self.view.keyPressed.connect(self.keyPressEvent)
        self.view.keyReleased.connect(self.keyReleaseEvent)
        self.view.quitApp.connect(self.quitApp)
        self.view.windowResize.connect(self.windowResize)
        self.view.windowHide.connect(self.windowHide)
        self.view.undoPress.connect(self.undo)
        self.view.redoPress.connect(self.redo)


    def actionPerformed(self, *args):
        eventSource = self.sender()
        print("trying to perform action: " + eventSource.text() + "_" + str(id(eventSource)))
        self.commandInvoker.executeCommand(eventSource, *args)

    def undo(self):
        self.commandInvoker.undoCommand()

    def redo(self):
        self.commandInvoker.redoCommand()

    # Key-Source:
    # https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.Key.html#Key_Q

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        if event.key() == QtCore.Qt.Key_Space:
            print("new figure")
            self.graphicsModel.addFigure()
            self.cvModel.trackingFlag = True

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.cvModel.trackingFlag = False

    def quitApp(self):
        # collect all threads
        self.cvModel.runningFlag = False
        print("exit clean Up")

    def windowResize(self, event):
        # force camera aspectratio to mainwindow
        oldSize = event.oldSize()
        size = event.size()
        vW = self.view.width()
        vH = self.view.height()
        if (oldSize == QSize(-1, -1)):  # ignore init size
            pass
        elif (size.width() != oldSize.width()):  # width changed
            vH = vW / self.aspectRatio
        else:  # height changed
            vW = vH * self.aspectRatio

        self.view.resize(vW, vH)
        cRect = QtCore.QRect(0, 0, vW, vH)
        self.view.getGraphicsView().setGeometry(cRect)


    def windowHide(self):
        print("window hide event")

    def windowActivate(self):
        print("window activate event")

