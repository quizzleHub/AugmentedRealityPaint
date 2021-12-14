class CommandInvoker:

    def __init__(self):
        self.commands = {}      #dict
        self.undoStack = []     #list
        self.redoStack = []     #list

    def addCommand(self, component, command):
        self.commands[component] = command

    def executeCommand(self, component):
        cmd = self.commands.get(component)
        cmd.execute()
        if (cmd.isUndoable()):          #if isUndoable
            self.undoStack.append(cmd)

    def undoCommand(self):
        if self.undoStack:              #if undoStack is not empty     
            cmd = self.undoStack.pop()
            self.redoStack.append(cmd)
            cmd.undo()
        else:
            print("undoStack is empty")
        
    def redoCommand(self):
        if self.redoStack:              #if redoStack is not empty
            cmd = self.redoStack.pop()
            self.undoStack.append(cmd)
            cmd.redo()
        else:
            print("redoStack is empty")
        