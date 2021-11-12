from commands.CommandInterface import CommandInterface


class CmdExportDrawing(CommandInterface):

    def __init__(self):
        self.view = None                
        self.model = None
    def execute(self):
        print("CmdExportDrawing executed")
    def redo(self):
        print("You cannot redo Export Drawing")
    def undo(self):
        print("You cannot undo Export Drawing")