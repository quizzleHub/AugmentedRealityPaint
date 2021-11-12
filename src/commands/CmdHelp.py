from commands.CommandInterface import CommandInterface


class CmdHelp(CommandInterface):

    def __init__(self):
        self.view = None                
        self.model = None
    def execute(self):
        print("CmdHelp executed")
    def redo(self):
        print("You cannot redo Help")
    def undo(self):
        print("You cannot undo Help")