from View import View
from commands.CommandInvoker import CommandInvoker
from commands.CmdCalibrateColor import CmdCalibrateColor
from commands.CmdExportDrawing import CmdExportDrawing
from commands.CmdHelp import CmdHelp
from commands.CmdOpenFile import CmdOpenFile
from commands.CmdPaint import CmdPaint
from commands.CmdSetStrokeColor import CmdSetStrokeColor
from commands.CmdSetStrokeWeight import CmdSetStrokeWeight



class BtnController:
    
    def __init__(self, view, model) -> None:
        self.view = view
        self.model = model
        self.commandInvoker = CommandInvoker()
        
    def registerEvents(self):

        
        btnButton1 = self.view.getbtnButton1()                          #get btnButton1
        btnButton2 = self.view.getbtnButton2()                          #get btnButton2
        lblLabel = self.view.getlblLabel()                              #get label

        btnButton1.pressed.connect(self.actionPerformed)   #register "pressed" event to actionPerformed
        btnButton2.pressed.connect(self.actionPerformed)

        print("registered events in BtnController")
        

    def registerCommands(self):
        self.commandInvoker.addCommand(self.view.getbtnButton1(), CmdSetStrokeWeight())     #register btnButton1 to CmdSetStrokeWeight -> Pressing Button1 will execute TestCommand          
        self.commandInvoker.addCommand(self.view.getbtnButton2(), CmdPaint())     #Was wenn zwei Buttons den selben Command aufrufen sollen? Evt Problem. ggfs alle commands zentral instanzieren
        print("registerd Commands in BtnController")



    def actionPerformed(self):
        eventSource = self.view.centralwidget.sender()                  #Problem: Was wenn kein centralwidget vorhanden ist??
        print("trying to perform action: " + eventSource.text() + "_" + str(id(eventSource)))
        self.commandInvoker.executeCommand(eventSource)


