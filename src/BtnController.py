from Main_view import MainView
from CommandInvoker import CommandInvoker
from commands.CmdAction import CmdAction
from commands.CmdUndo import CmdUndo
from commands.CmdRedo import CmdRedo
from PyQt5.QtCore import QObject, pyqtSlot


class BtnController(QObject): #windowListener, ActionListener
    
    def __init__(self, view, cvModel):
        super().__init__()
        self.view = view
        self.cvModel = cvModel
        self.commandInvoker = CommandInvoker()

        #all buttons
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
        self.cmdAction = CmdAction()
        self.cmdRedo = CmdRedo()
        self.cmdUndo = CmdUndo()
        
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


        #custom events
        self.view.keyPressed.connect(self.keyPressEvent)
        self.view.quitApp.connect(self.quitApp)
        self.view.windowResize.connect(self.windowResize)
        self.view.windowHide.connect(self.windowHide)
        self.view.windowActivate.connect(self.windowActivate)
        self.btnUndo.triggered.connect(self.undo)
        self.btnRedo.triggered.connect(self.redo)
    

        print("registered events in BtnController")
        

    def registerCommands(self):
        #register buttons to commands
        self.commandInvoker.addCommand(self.btnNeu, self.cmdAction)
        self.commandInvoker.addCommand(self.btnOeffnen, self.cmdAction)
        self.commandInvoker.addCommand(self.btnSpeichern, self.cmdAction)
        self.commandInvoker.addCommand(self.btnExportieren, self.cmdAction)
        self.commandInvoker.addCommand(self.btnKallibrieren, self.cmdAction)
        self.commandInvoker.addCommand(self.btnHilfe, self.cmdAction)
        self.commandInvoker.addCommand(self.btnZeichnen, self.cmdAction)
        self.commandInvoker.addCommand(self.btnRadieren, self.cmdAction)
        self.commandInvoker.addCommand(self.btnRot, self.cmdAction)
        self.commandInvoker.addCommand(self.btnGruen, self.cmdAction)
        self.commandInvoker.addCommand(self.btnBlau, self.cmdAction)
        self.commandInvoker.addCommand(self.btnGelb, self.cmdAction)
        self.commandInvoker.addCommand(self.btnWeiss, self.cmdAction)
        self.commandInvoker.addCommand(self.btnSchwarz, self.cmdAction)
        self.commandInvoker.addCommand(self.btnDick, self.cmdAction)
        self.commandInvoker.addCommand(self.btnMittel, self.cmdAction)
        self.commandInvoker.addCommand(self.btnDuenn, self.cmdAction)

        self.commandInvoker.addCommand(self.btnUndo, self.cmdUndo)    
        self.commandInvoker.addCommand(self.btnRedo, self.cmdRedo)

        print("registerd Commands in BtnController")


    def actionPerformed(self):
        eventSource = self.sender()
        print("trying to perform action: " + eventSource.text() + "_" + str(id(eventSource)))
        self.commandInvoker.executeCommand(eventSource)



    def undo(self):
        self.commandInvoker.undoCommand()

    def redo(self):
        self.commandInvoker.redoCommand()

    def keyPressEvent(self):
            print("keyPressEvent")

    def quitApp(self):
        #collect all threads
        self.cvModel.stop()
        print("Exit Clean Up")

    def windowResize(self):
        print("window resized")

    def windowHide(self):
        print("window hide event")
    
    def windowActivate(self):
        print("Window activate event")



