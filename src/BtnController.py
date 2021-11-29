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
        
    def registerEvents(self):

        btnRot = self.view.getbtnRot()
        btnUndo = self.view.getbtnUndo()                #get btnUndo
        btnRedo = self.view.getbtnRedo()                #get btnRedo


        #custom events
        self.view.keyPressed.connect(self.keyPressEvent)
        self.view.quitApp.connect(self.quitApp)
        self.view.windowResize.connect(self.windowResize)
        self.view.windowHide.connect(self.windowHide)
        self.view.windowActivate.connect(self.windowActivate)


        #register event to actionPerformed for all buttons
        btnRot.triggered.connect(self.actionPerformed) 
        btnUndo.triggered.connect(self.actionPerformed)
        btnRedo.triggered.connect(self.actionPerformed)



    

        print("registered events in BtnController")
        

    def registerCommands(self):
        self.commandInvoker.addCommand(self.view.getbtnRot(), CmdAction())   #register btnButton1 to CmdSetStrokeWeight -> Pressing Button1 will execute TestCommand          
        self.commandInvoker.addCommand(self.view.getbtnUndo(), CmdUndo())       #Was wenn zwei Buttons den selben Command aufrufen sollen? Evt Problem. ggfs alle commands zentral instanzieren
        self.commandInvoker.addCommand(self.view.getbtnRedo(), CmdRedo())

        print("registerd Commands in BtnController")


    def actionPerformed(self):
        eventSource = self.app.sender()
        print("trying to perform action: " + eventSource.text() + "_" + str(id(eventSource)))

        if (eventSource == self.view.getbtnUndo()):
            self.commandInvoker.undoCommand()
        elif(eventSource == self.view.getbtnRedo()):
            self.commandInvoker.redoCommand()
        else:
            self.commandInvoker.executeCommand(eventSource)

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



