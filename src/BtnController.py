from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from Main_view import MainView

from CommandInvoker import CommandInvoker
from commands.CmdAction import CmdAction
from commands.CmdCalibrateCVCol import CmdCalibrateCVCol
from commands.CmdSetStrokeColor import CmdSetStrokeColor

class BtnController(QObject): #windowListener, ActionListener
    
    def __init__(self, view, cvModelThread, cvModel, grafikModel):
        super().__init__()
        self.view = view
        self.cvModelThread = cvModelThread
        self.cvModel = cvModel
        self.grafikModel = grafikModel
        self.commandInvoker = CommandInvoker()
        #self.aspectRatio = cvModel.getAspectRatio()

        #get buttons
        self.btnNeu = self.view.getbtnNeu()
        self.btnOeffnen = self.view.getbtnOeffnen()
        self.btnSpeichern = self.view.getbtnSpeichern()
        self.btnExportieren = self.view.getbtnExportieren()
        self.btnKallibrieren = self.view.getbtnKalibrieren()
        self.btnHilfe = self.view.getbtnHilfe()
        self.btnZeichnen = self.view.getbtnHilfe()
        self.btnRadieren = self.view.getbtnRadieren()
        self.btnRot = self.view.getbtnRot()
        self.btnGruen = self.view.getbtnGruen()
        self.btnBlau = self.view.getbtnBlau()
        self.btnGelb = self.view.getbtnGelb()
        self.btnWeiss = self.view.getbtnWeiss()
        self.btnSchwarz = self.view.getbtnSchwarz()
        self.btnDick = self.view.getbtnDick()
        self.btnMittel = self.view.getbtnMittel()
        self.btnDuenn = self.view.getbtnDuenn()
        self.btnUndo = self.view.getbtnUndo()
        self.btnRedo = self.view.getbtnRedo()
        
        #all commands
        self.cmdAction = CmdAction(self.view, self.cvModel)
        self.cmdSetStrokeColor = CmdSetStrokeColor(self.view, self.cvModel)
        self.cmdCalibrateCVCol = CmdCalibrateCVCol(self.view, self.cvModel)
        #etc...

        
    def registerEvents(self):
        #register event to actionPerformed for all buttons
        self.btnNeu.triggered.connect(self.actionPerformed)
        self.btnOeffnen.triggered.connect(self.actionPerformed) 
        self.btnSpeichern.triggered.connect(self.actionPerformed) 
        self.btnExportieren.triggered.connect(self.actionPerformed) 
        self.btnKallibrieren.triggered.connect(self.actionPerformed) 
        self.btnHilfe.triggered.connect(self.actionPerformed) 
        self.btnZeichnen.triggered.connect(self.actionPerformed) 
        self.btnRadieren.triggered.connect(self.actionPerformed) 
        self.btnRot.triggered.connect(self.actionPerformed) 
        self.btnGruen.triggered.connect(self.actionPerformed) 
        self.btnBlau.triggered.connect(self.actionPerformed) 
        self.btnGelb.triggered.connect(self.actionPerformed) 
        self.btnWeiss.triggered.connect(self.actionPerformed) 
        self.btnSchwarz.triggered.connect(self.actionPerformed) 
        self.btnDick.triggered.connect(self.actionPerformed) 
        self.btnMittel.triggered.connect(self.actionPerformed) 
        self.btnDuenn.triggered.connect(self.actionPerformed) 
    
        print("registered events in BtnController")
        
    def registerCommands(self):
        #register buttons to commands
        self.commandInvoker.addCommand(self.btnNeu, self.cmdAction)
        self.commandInvoker.addCommand(self.btnOeffnen, self.cmdAction)
        self.commandInvoker.addCommand(self.btnSpeichern, self.cmdAction)
        self.commandInvoker.addCommand(self.btnExportieren, self.cmdAction)
        self.commandInvoker.addCommand(self.btnKallibrieren, self.cmdCalibrateCVCol)
        self.commandInvoker.addCommand(self.btnHilfe, self.cmdAction)
        self.commandInvoker.addCommand(self.btnZeichnen, self.cmdAction)
        self.commandInvoker.addCommand(self.btnRadieren, self.cmdAction)
        self.commandInvoker.addCommand(self.btnRot, self.cmdSetStrokeColor)
        self.commandInvoker.addCommand(self.btnGruen, self.cmdAction)
        self.commandInvoker.addCommand(self.btnBlau, self.cmdAction)
        self.commandInvoker.addCommand(self.btnGelb, self.cmdAction)
        self.commandInvoker.addCommand(self.btnWeiss, self.cmdAction)
        self.commandInvoker.addCommand(self.btnSchwarz, self.cmdAction)
        self.commandInvoker.addCommand(self.btnDick, self.cmdAction)
        self.commandInvoker.addCommand(self.btnMittel, self.cmdAction)
        self.commandInvoker.addCommand(self.btnDuenn, self.cmdAction)

        print("registerd Commands in BtnController")

    def connectSignals(self):
        self.cvModelThread.started.connect(self.cvModel.run)
        self.cvModel.newCamFrame.connect(self.view.grafikView.updateCanvas)
        self.cvModel.newTrackedCoords.connect(self.grafikModel.addPoint)
        self.cvModel.exitSig.connect(self.cvModelThread.quit)

        self.view.keyPressed.connect(self.keyPressEvent)
        self.view.keyReleased.connect(self.keyReleaseEvent)
        #self.view.canvasPressed.connect(self.canvasClick)
        self.view.quitApp.connect(self.quitApp)
        self.view.windowResize.connect(self.windowResize)
        self.view.windowHide.connect(self.windowHide)
        self.view.undoPress.connect(self.undo)
        self.view.redoPress.connect(self.redo)
        #self.view.windowActivate.connect(self.windowActivate)

    def actionPerformed(self):
        eventSource = self.sender()
        print("trying to perform action: " + eventSource.text() + "_" + str(id(eventSource)))
        self.commandInvoker.executeCommand(eventSource)
        
    def undo(self):
        self.commandInvoker.undoCommand()

    def redo(self):
        self.commandInvoker.redoCommand()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        if event.key() == QtCore.Qt.Key_Space:
            print("new figure")
            self.grafikModel.addFigure()
            self.cvModel.trackingFlag = True

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.cvModel.trackingFlag = False

            
    def quitApp(self):
        #collect all threads
        self.cvModel.runningFlag = False
        print("exit clean Up")

    def windowResize(self):
        #get aspect ratio
        #get width
        #calc height
        #cW = self.view.width()
        #cH = self.view.height()

        #cH = self.view.height()-4
        #cHAR = cW/self.aspectRatio
        #cWAR = self.aspectRatio * cHAR
        #cRect = QtCore.QRect(0,0,cWAR,cHAR)
        #self.view.getGraphicsView().setGeometry(cRect)
        #self.view.getGraphicsView().update()
        pass

    def windowHide(self):
        print("window hide event")
    
    def windowActivate(self):
        print("window activate event")

