from commands.CommandInterface import CommandInterface



class CmdSetStrokeWidth(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = False
    def execute(self, *args):
        self.view.grafikView.setStrokeWidth(args[0])
        print("CmdSetStrokeWidth executed")      
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool