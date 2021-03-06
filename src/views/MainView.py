from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QEvent, pyqtSignal
from views.View_ui_rcs import Ui_View


class MainView(QMainWindow):

    ##pyqtSignals
    keyPressed = pyqtSignal(QEvent)
    keyReleased = pyqtSignal(QEvent)
    canvasPressed = pyqtSignal(QEvent)
    quitApp = pyqtSignal(QEvent)
    windowResize = pyqtSignal(QEvent)
    windowHide = pyqtSignal(QEvent)

    def __init__(self, graphicsView):
        super().__init__()
        self._ui = Ui_View()
        self._ui.setupUi(self)
        self.graphicsView = graphicsView
        self._ui.graphicsView.mousePressEvent = self.canvasPressedEvent

    def keyPressEvent(self, event):
        super(MainView, self).keyPressEvent(event)
        self.keyPressed.emit(event)

    def keyReleaseEvent(self, event):
        super(MainView, self).keyReleaseEvent(event)
        self.keyReleased.emit(event)

    def canvasPressedEvent(self, event):
        self.canvasPressed.emit(event)
        
    def closeEvent(self, event):
        super(MainView,self).closeEvent(event)
        self.quitApp.emit(event)

    def resizeEvent(self, event):
        super(MainView,self).resizeEvent(event)
        self.windowResize.emit(event)
    
    def hideEvent(self, event):
        super(MainView, self).hideEvent(event)
        self.windowHide.emit(event)

    #_____Getter______
    def getGraphicsView(self):
        return self._ui.graphicsView

    def getbtnFile(self):
        return self._ui.menuFile

    def getbtnClear_all(self):
        return self._ui.actionClear_all

    def getbtnOpen(self):
        return self._ui.actionOpen

    def getbtnSave(self):
        return self._ui.actionSave

    def getbtnExportNB(self):
        return self._ui.actionwithout_Camera_Background

    def getbtnExportWB(self):
        return self._ui.actionwith_Camera_Background

    def getbtnCalibrate(self):
        return self._ui.actionCalibrate

    def getbtnHelp(self):
        return self._ui.actionHelp

    def getbtnPaint(self):
        return self._ui.actionPaint

    def getbtnErase(self):
        return self._ui.actionErase

    def getbtnRed(self):
        return self._ui.actionRed

    def getbtnBlue(self):
        return self._ui.actionBlue

    def getbtnYellow(self):
        return self._ui.actionYellow

    def getbtnThick(self):
        return self._ui.actionThick

    def getbtnMedium(self):
        return self._ui.actionMedium

    def getbtnThin(self):
        return self._ui.actionThin
    
    def getbtnColorPicker(self):
        return self._ui.actionColorpicker

    def getbtnStrokeWidthPicker(self):
        return self._ui.actionStrokewidth
