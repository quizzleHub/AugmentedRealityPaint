

class CommandInvoker:

    def __init__(self):
        self.commands = {}   #dict

    def addCommand(self, component, command):
        self.commands[component] = command

    def executeCommand(self, component):
        self.commands.get(component).execute()
        #undoStack.push(commands.get(key))