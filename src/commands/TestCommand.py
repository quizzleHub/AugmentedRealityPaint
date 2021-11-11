from commands.CommandInterface import CommandInterface


class TestCommand(CommandInterface):
    view = None
    model = None

    def __init__(self):
        self.view = None                ###None??
        self.model = None
    def execute(self):
        print("Test Command execute")
    def redo(self):
        print("Test Command redo")
    def undo(self):
        print("Test Command undo")