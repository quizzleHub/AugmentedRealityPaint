from commands.CommandInterface import CommandInterface


class CmdOpenFile(CommandInterface):

    def __init__(self):
        self.view = None                
        self.model = None
    def execute(self):
        print("CmdOpenFile executed")
    def redo(self):
        print("You cannot redo Open File")
    def undo(self):
        print("You cannot undo Open File")