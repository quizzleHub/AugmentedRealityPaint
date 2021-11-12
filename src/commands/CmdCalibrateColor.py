from commands.CommandInterface import CommandInterface


class CmdCalibrateColor(CommandInterface):

    def __init__(self):
        self.view = None                
        self.model = None
    def execute(self):
        print("CmdCalibrateColor executed")
    def redo(self):
        print("You cannot redo Calibrate Color")
    def undo(self):
        print("You cannot undo Calibrate Color")