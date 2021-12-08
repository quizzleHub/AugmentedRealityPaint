from CommandInterface import CommandInterface


class CmdSafeFigures(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = False
    def execute(self):
        print("SafeFigures executed")
        self.model.safeFigures()
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool
