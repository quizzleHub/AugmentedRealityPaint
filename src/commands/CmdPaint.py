from commands.CommandInterface import CommandInterface


class CmdPaint(CommandInterface):

    def __init__(self):
        self.view = None                
        self.model = None
    def execute(self):
        print("CmdPaint executed")
    def redo(self):
        print("CmdPaint redo")
    def undo(self):
        print("CmdPaint undo")