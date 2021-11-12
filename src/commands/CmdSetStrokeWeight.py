from commands.CommandInterface import CommandInterface


class CmdSetStrokeWeight(CommandInterface):

    def __init__(self):
        self.view = None                
        self.model = None
    def execute(self):
        print("CmdSetStrokeWeight executed")
    def redo(self):
        print("CmdSetStrokeWeight redo")
    def undo(self):
        print("CmdSetStrokeWeight undo")