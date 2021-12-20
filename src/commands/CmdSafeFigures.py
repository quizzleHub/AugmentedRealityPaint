from commands.CommandInterface import CommandInterface


class CmdSafeFigures(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = False

    def execute(self, *args):
        self.model.safeFigures()

    def redo(self):
        pass

    def undo(self):
        pass
    
    def isUndoable(self):
        return self.isUndoableBool
