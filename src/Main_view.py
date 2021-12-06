"""
Use Qt designer to create the .ui layout files to the extent that you assign variables names to widgets and adjust their basic properties. Don't bother adding signals or slots as it's generally easier just to connect them to functions from within the view class.

The .ui layout files are converted to .py layout files when processed with pyuic or pyside-uic. The .py view files can then import the relevant auto-generated classes from the .py layout files.

The view class(es) should contain the minimal code required to connect to the signals coming from the widgets in your layout. View events can call and pass basic information to a method in the view class and onto a method in a controller class, where any logic should be. 
"""




from threading import Event
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot, QEvent, pyqtSignal
from PyQt5.QtGui import QKeyEvent
from View_ui_rcs import Ui_View






class MainView(QMainWindow):

    ##pyqtSignals
    keyPressed = pyqtSignal(QEvent)
    canvasPressed = pyqtSignal(QEvent)
    quitApp = pyqtSignal(QEvent)
    windowResize = pyqtSignal(QEvent)
    windowHide = pyqtSignal(QEvent)
    #windowActivate = pyqtSignal(QEvent)
    redoPress = pyqtSignal(QEvent)
    undoPress = pyqtSignal(QEvent)
 


    def __init__(self, grafikView):
        super().__init__()

        
        self._ui = Ui_View()
        self._ui.setupUi(self)
        self.grafikView = grafikView
        self._ui.menuUndo.mousePressEvent = self.undoEvent
        self._ui.menuRedo.mousePressEvent = self.redoEvent
        self._ui.GraphicsView.mousePressEvent = self.canvasPressedEvent


        
        


    #_____emit events______
    # all possible events: https://doc.qt.io/qt-5/qevent.html
    def keyPressEvent(self, event):
        super(MainView, self).keyPressEvent(event)
        self.keyPressed.emit(event)

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


    
    """
    def changeEvent(self, event):
        #______FUNZT nicht________!
        # hex codes for events
        #https://doc.qt.io/qt-5/qt.html#WindowState-enum
        #if event.type() == QEvent.ActivationChange:  #changed state of window
        #print(event.type())


        if (self.windowState() == 0x00000001):      #window minimzed
            print("window min")
        elif(self.windowState() == 0x00000002):     #window maximized
            print("win max")
        elif(self.windowState() == 0x00000004):     #window fullscreen
            print("win fullscr")
        elif(self.windowState() == 0x00000008):     #window activated (focused)
            print("win foc")
    """


    #_____Getter______
    def getGraphicsView(self):
        return self._ui.GraphicsView


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
