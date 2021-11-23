from View import View
from CommandInvoker import CommandInvoker
from commands.CmdAction import CmdAction
from commands.CmdUndo import CmdUndo
from commands.CmdRedo import CmdRedo




class BtnController: #windowListener, ActionListener
    
    def __init__(self, view, cvModel, app) -> None:
        self.view = view
        self.cvModel = cvModel
        self.app = app
        self.commandInvoker = CommandInvoker()
        
    def registerEvents(self):

        btnAction = self.view.getbtnAction()            #get btnAction
        btnUndo = self.view.getbtnUndo()                #get btnUndo
        btnRedo = self.view.getbtnRedo()                #get btnRedo
        lblLabel = self.view.getlblLabel()              #get lblLabel

        #register "pressed" event to actionPerformed for all buttons
        btnAction.pressed.connect(self.actionPerformed) 
        btnUndo.pressed.connect(self.actionPerformed)
        btnRedo.pressed.connect(self.actionPerformed)

        self.app.aboutToQuit.connect(self.onExit)   #closing app
        



        

        print("registered events in BtnController")
        

    def registerCommands(self):
        self.commandInvoker.addCommand(self.view.getbtnAction(), CmdAction())   #register btnButton1 to CmdSetStrokeWeight -> Pressing Button1 will execute TestCommand          
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

    def onExit(self):
        #collect all threads
        self.cvModel.stop()
        print("Exit Clean Up")



