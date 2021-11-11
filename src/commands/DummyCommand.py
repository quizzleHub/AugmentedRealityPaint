from commands.CommandInterface import CommandInterface


class DummyCommand(CommandInterface):
    view = None
    model = None

    def __init__(self):
        self.view = None                ###None??
        self.model = None
    def execute(self):
        print("DummyCommand executed")
    def redo(self):
        print("DummyCommand redo")
    def undo(self):
        print("DummyCommand undo")