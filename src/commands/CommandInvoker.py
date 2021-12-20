class CommandInvoker:

    def __init__(self):
        self.commands = {}
        self.undoStack = []
        self.redoStack = []

    def addCommand(self, component, command):
        self.commands[component] = command

    def executeCommand(self, component, *args):
        cmd = self.commands.get(component)
        cmd.execute(*args)
        if (cmd.isUndoable()):
            self.undoStack.append(cmd)

    def undoCommand(self):
        if self.undoStack:   
            cmd = self.undoStack.pop()
            self.redoStack.append(cmd)
            cmd.undo()
        else:
            print("undoStack is empty")
        
    def redoCommand(self):
        if self.redoStack:
            cmd = self.redoStack.pop()
            self.undoStack.append(cmd)
            cmd.redo()
        else:
            print("redoStack is empty")
        