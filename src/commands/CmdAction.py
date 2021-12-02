from CommandInterface import CommandInterface


class CmdAction(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = True
    def execute(self):
        print("Action executed")
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool
