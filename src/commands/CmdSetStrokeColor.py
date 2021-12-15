from commands.CommandInterface import CommandInterface



class CmdSetStrokeColor(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = False
    def execute(self, *args):
        self.view.graphicsView.setStrokeColor(args[0])
        print("CmdSetStrokeColor executed")   
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool