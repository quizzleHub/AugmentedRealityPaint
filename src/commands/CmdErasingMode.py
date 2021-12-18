from commands.CommandInterface import CommandInterface


class CmdErasingMode(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = False
    def execute(self, *args):
        self.model.setMode(1)
    def redo(self):
        pass
    def undo(self):
        pass
    def isUndoable(self):
        return self.isUndoableBool