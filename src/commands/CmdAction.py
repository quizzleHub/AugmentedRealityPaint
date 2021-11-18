from CommandInterface import CommandInterface


class CmdAction(CommandInterface):

    def __init__(self):
        self.view = None                
        self.model = None
        self.isUndoableBool = True
    def execute(self):
        print("Action executed")
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool
