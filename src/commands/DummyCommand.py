from commands.CommandInterface import CommandInterface


class DummyCommand(CommandInterface):

    def __init__(self):
        self.view = None                
        self.model = None
    def execute(self):
        print("DummyCommand executed")
    def redo(self):
        print("DummyCommand redo")
    def undo(self):
        print("DummyCommand undo")