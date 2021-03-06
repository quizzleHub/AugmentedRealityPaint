from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QSize
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QColorDialog
from commands.CmdHelp import CmdHelp

from commands.CommandInvoker import CommandInvoker
from commands.CmdCalibrateCVCol import CmdCalibrateCVCol
from commands.CmdSafeFigures import CmdSafeFigures
from commands.CmdOpenFigures import CmdOpenFigures
from commands.CmdClearFigures import CmdClearFigures
from commands.CmdSetStrokeColor import CmdSetStrokeColor
from commands.CmdDrawingMode import CmdDrawingMode
from commands.CmdErasingMode import CmdErasingMode
from commands.CmdSetStrokeColor import CmdSetStrokeColor
from commands.CmdSetStrokeWidth import CmdSetStrokeWidth
from commands.CmdExportDwgNB import CmdExportDrawingNB
from commands.CmdExportDwgWB import CmdExportDrawingWB


class MainController(QObject):

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
        self.btnExportWB = self.view.getbtnExportWB()
        self.btnExportNB = self.view.getbtnExportNB()
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
        self.btnColorPicker = self.view.getbtnColorPicker()
        self.btnStrokeWidthPicker = self.view.getbtnStrokeWidthPicker()

        # all commands
        self.cmdCalibrateCVCol = CmdCalibrateCVCol(self.view, self.cvModel)
        self.cmdSafeFigures = CmdSafeFigures(self.view, self.graphicsModel)
        self.cmdOpenFigures = CmdOpenFigures(self.view, self.graphicsModel)
        self.cmdClearFigures = CmdClearFigures(self.view, self.graphicsModel)
        self.cmdSetStrokeColor = CmdSetStrokeColor(self.view, self.graphicsModel)
        self.cmdSetStrokeWidth = CmdSetStrokeWidth(self.view, self.graphicsModel)
        self.cmdDrawingMode = CmdDrawingMode(self.view, self.graphicsModel)
        self.cmdErasingMode = CmdErasingMode(self.view, self.graphicsModel)
        self.cmdExportDrawingNB = CmdExportDrawingNB(self.view, self.graphicsModel, self.cvModel)
        self.cmdExportDrawingWB = CmdExportDrawingWB(self.view, self.graphicsModel, self.cvModel)
        self.cmdHelp = CmdHelp(self.view, self.cvModel)

        # set correct window aspectratio for camera
        self.aspectRatio = self.cvModel.aspectRatio
        self.view.resize(self.view.width(), self.view.width() / self.aspectRatio)

        # preset for buttons
        self.view.getbtnPaint().setChecked(True)
        self.view.getbtnRed().setChecked(True)
        self.view.getbtnMedium().setChecked(True)

    def registerEvents(self):
        # register event to actionPerformed for all buttons
        self.btnClear_all.triggered.connect(self.actionPerformed)
        self.btnOpen.triggered.connect(self.actionPerformed)
        self.btnSave.triggered.connect(self.actionPerformed)
        self.btnExportNB.triggered.connect(self.actionPerformed)
        self.btnExportWB.triggered.connect(self.actionPerformed)
        self.btnCalibrate.triggered.connect(self.actionPerformed)
        self.btnHelp.triggered.connect(self.actionPerformed)

        self.btnPaint.triggered.connect(self.actionPerformed)
        self.btnErase.triggered.connect(self.actionPerformed)

        self.btnBlue.triggered.connect(lambda: self.actionPerformed(QColor(102, 140, 255), self.btnBlue))
        self.btnYellow.triggered.connect(lambda: self.actionPerformed(QColor(255,255,128), self.btnYellow))
        self.btnRed.triggered.connect(lambda: self.actionPerformed(QColor(255,102,102), self.btnRed))
        self.btnColorPicker.triggered.connect(lambda: self.actionPerformed(QColorDialog.getColor(), self.btnColorPicker))
        self.btnThick.triggered.connect(lambda: self.actionPerformed(7.3, self.btnThick))
        self.btnMedium.triggered.connect(lambda: self.actionPerformed(4.3, self.btnMedium))
        self.btnThin.triggered.connect(lambda: self.actionPerformed(1.3, self.btnThin))
        self.btnStrokeWidthPicker.triggered.connect(lambda: self.actionPerformed(None, self.btnStrokeWidthPicker))

    def connectSignals(self):
        self.cvModelThread.started.connect(self.cvModel.run)
        self.cvModel.newCamFrame.connect(self.view.graphicsView.updateCanvas)
        self.cvModel.newTrackedCoords.connect(self.graphicsModel.recPoint)
        self.cvModel.exitSig.connect(self.cvModelThread.quit)

        self.view.keyPressed.connect(self.keyPressEvent)
        self.view.keyReleased.connect(self.keyReleaseEvent)
        self.view.quitApp.connect(self.quitApp)
        self.view.windowResize.connect(self.windowResize)
        self.view.windowHide.connect(self.windowHide)

    def registerCommands(self):
        self.commandInvoker.addCommand(self.btnOpen, self.cmdOpenFigures)
        self.commandInvoker.addCommand(self.btnSave, self.cmdSafeFigures)
        self.commandInvoker.addCommand(self.btnClear_all, self.cmdClearFigures)
        self.commandInvoker.addCommand(self.btnExportNB, self.cmdExportDrawingNB)
        self.commandInvoker.addCommand(self.btnExportWB, self.cmdExportDrawingWB)
        self.commandInvoker.addCommand(self.btnCalibrate, self.cmdCalibrateCVCol)
        self.commandInvoker.addCommand(self.btnHelp, self.cmdHelp)

        self.commandInvoker.addCommand(self.btnPaint, self.cmdDrawingMode)
        self.commandInvoker.addCommand(self.btnErase, self.cmdErasingMode)

        self.commandInvoker.addCommand(self.btnBlue, self.cmdSetStrokeColor)
        self.commandInvoker.addCommand(self.btnYellow, self.cmdSetStrokeColor)
        self.commandInvoker.addCommand(self.btnRed, self.cmdSetStrokeColor)
        self.commandInvoker.addCommand(self.btnColorPicker, self.cmdSetStrokeColor)

        self.commandInvoker.addCommand(self.btnThick, self.cmdSetStrokeWidth)
        self.commandInvoker.addCommand(self.btnMedium, self.cmdSetStrokeWidth)
        self.commandInvoker.addCommand(self.btnThin, self.cmdSetStrokeWidth)
        self.commandInvoker.addCommand(self.btnStrokeWidthPicker, self.cmdSetStrokeWidth)

    def actionPerformed(self, *args):
        eventSource = self.sender()
        self.commandInvoker.executeCommand(eventSource, *args)

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        if event.key() == QtCore.Qt.Key_Space:
            #if drawingMode
            if self.graphicsModel.getMode() == 0:   
                #create new figure where CVModel can append points
                strokeColor = self.view.graphicsView.getStrokeColor()
                strokeWidth = self.view.graphicsView.getStrokeWidth()
                strokePattern = self.view.graphicsView.getStrokePattern()
                brushStyle = self.view.graphicsView.getBrushStyle()
                penCapStyle = self.view.graphicsView.getPenCapStyle()
                self.graphicsModel.addFigure(strokeColor, strokeWidth, strokePattern, brushStyle, penCapStyle) 
            #turn on tracking in CVModel
            self.cvModel.trackingFlag = True

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            #turn off tracking in CVModel
            self.cvModel.trackingFlag = False
            #if drawingMode
            if self.graphicsModel.getMode() == 0:   
                #check if last figure is empty and delete it
                figure = self.graphicsModel.getLastFigure()
                points = figure.getPoints()
                if not points:
                    self.graphicsModel.deleteLastFigure()

    def quitApp(self):
        # collect all threads
        self.cvModel.runningFlag = False

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
        pass

    def windowActivate(self):
        pass

    def startUp(self):
        self.cmdCalibrateCVCol.execute()
