from CommandInterface import CommandInterface


class CmdRedo(CommandInterface):

    def __init__(self):
        self.view = None                
        self.model = None
        self.isUndoableBool = False
    def execute(self):
        print("Redo executed")
    def redo(self):
        print("Redo cannot be redone")
    def undo(self):
        print("Redo cannot be undone")
    def isUndoable(self):
        return self.isUndoableBool