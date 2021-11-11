from View import View
from commands.CommandInvoker import CommandInvoker
from commands.TestCommand import TestCommand
from commands.DummyCommand import DummyCommand
#from PyQt5.QtCore import * #signal mapper


class BtnController:

    view = None
    model = None
    commandInvoker = None

    
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
        self.commandInvoker.addCommand(self.view.getbtnButton1(), TestCommand())            #register btnButton1 to TestCommand -> Pressing Button one will execute TestCommand
        self.commandInvoker.addCommand(self.view.getbtnButton2(), DummyCommand())            #Was wenn zwei Buttons den selben Command aufrufen sollen? Evt Problem. ggfs alle commands zentral instanzieren
        print("registerd Commands in BtnController")



    def actionPerformed(self):
        eventSource = self.view.centralwidget.sender()
        print("trying to perform action: execute command by: " + eventSource.text() + "_" + str(id(eventSource)))
        self.commandInvoker.executeCommand(eventSource)


