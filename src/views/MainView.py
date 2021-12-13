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
    redoPress = pyqtSignal(QEvent)
    undoPress = pyqtSignal(QEvent)
 


    def __init__(self, grafikView):
        super().__init__()

        
        self._ui = Ui_View()
        self._ui.setupUi(self)
        self.grafikView = grafikView
        self._ui.menuUndo.mousePressEvent = self.undoEvent
        self._ui.menuRedo.mousePressEvent = self.redoEvent
        self._ui.graphicsView.mousePressEvent = self.canvasPressedEvent


    #_____emit events______
    # all possible events: https://doc.qt.io/qt-5/qevent.html
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

    def undoEvent(self, event):
        self.undoPress.emit(event)

    def redoEvent(self, event):
        self.redoPress.emit(event)



    #_____Getter______
    def getGraphicsView(self):
        return self._ui.graphicsView

    def getbtnOptionen(self):
        return self._ui.menuOptionen

    def getbtnNeu(self):
        return self._ui.actionNeu

    def getbtnOeffnen(self):
        return self._ui.actionOeffnen

    def getbtnSpeichern(self):
        return self._ui.actionSpeichern

    def getbtnExportieren(self):
        return self._ui.actionExportieren

    def getbtnKalibrieren(self):
        return self._ui.actionKalibrieren

    def getbtnHilfe(self):
        return self._ui.actionHilfe

    def getbtnZeichnen(self):
        return self._ui.menuZeichnen

    def getbtnRadieren(self):
        return self._ui.menuRadieren

    def getbtnFarbe(self):
        return self._ui.menuFarbe

    def getbtnRot(self):
        return self._ui.actionrot

    def getbtnGruen(self):
        return self._ui.actiongruen

    def getbtnBlau(self):
        return self._ui.actionblau

    def getbtnGelb(self):
        return self._ui.actiongelb

    def getbtnWeiss(self):
        return self._ui.actionweiss

    def getbtnSchwarz(self):
        return self._ui.actionschwarz

    def getbtnStrichdicke(self):
        return self._ui.menuStrichdicke

    def getbtnDick(self):
        return self._ui.actionDick

    def getbtnMittel(self):
        return self._ui.actionMittel

    def getbtnDuenn(self):
        return self._ui.actionDuenn

    def getbtnUndo(self):
        return self._ui.menuUndo

    def getbtnRedo(self):
        return self._ui.menuRedo
    
    def getCentralWidget(self):
        return self._ui.centralwidget
