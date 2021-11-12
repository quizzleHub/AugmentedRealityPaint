from commands.CommandInterface import CommandInterface


class CmdSetStrokeColor(CommandInterface):

    def __init__(self):
        self.view = None                
        self.model = None
    def execute(self):
        print("CmdSetStrokeColor executed")
    def redo(self):
        print("CmdSetStrokeColor redo")
    def undo(self):
        print("CmdSetStrokeColor undo")