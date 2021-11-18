from CommandInterface import CommandInterface


class CmdUndo(CommandInterface):

    def __init__(self):
        self.view = None                
        self.model = None
        self.isUndoableBool = False
    def execute(self):
        print("Undo executed")
    def redo(self):
        print("Undo cannot be redone")
    def undo(self):
        print("Undo cannot be undone")
    def isUndoable(self):
        return self.isUndoableBool