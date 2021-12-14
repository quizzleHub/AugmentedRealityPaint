from commands.CommandInterface import CommandInterface


class CmdClearFigures(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = False
    def execute(self):
        print("ClearFigures executed")
        self.model.clearFigures()
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool
