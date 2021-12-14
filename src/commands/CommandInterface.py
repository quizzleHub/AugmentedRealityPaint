class CommandInterface:
    def __init__(self):
        self.isUndoableBool: bool
    def execute(self):
        pass
    def undo(self):
        pass
    def redo(self):
        pass
    def isUndoable(self):
        return self.isUndoableBool