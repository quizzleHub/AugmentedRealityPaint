from View import View
from CommandInvoker import CommandInvoker
from commands.CmdAction import CmdAction
from commands.CmdUndo import CmdUndo
from commands.CmdRedo import CmdRedo




class BtnController:
    
    def __init__(self, view, model) -> None:
        self.view = view
        self.model = model
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

        print("registered events in BtnController")
        

    def registerCommands(self):
        self.commandInvoker.addCommand(self.view.getbtnAction(), CmdAction())   #register btnButton1 to CmdSetStrokeWeight -> Pressing Button1 will execute TestCommand          
        self.commandInvoker.addCommand(self.view.getbtnUndo(), CmdUndo())       #Was wenn zwei Buttons den selben Command aufrufen sollen? Evt Problem. ggfs alle commands zentral instanzieren
        self.commandInvoker.addCommand(self.view.getbtnRedo(), CmdRedo())
        print("registerd Commands in BtnController")


    def actionPerformed(self):
        eventSource = self.view.centralwidget.sender()                  #Problem: Was wenn kein centralwidget vorhanden ist??
        print("trying to perform action: " + eventSource.text() + "_" + str(id(eventSource)))

        if (eventSource == self.view.getbtnUndo()):
            self.commandInvoker.undoCommand()
        elif(eventSource == self.view.getbtnRedo()):
            self.commandInvoker.redoCommand()
        else:
            self.commandInvoker.executeCommand(eventSource)




