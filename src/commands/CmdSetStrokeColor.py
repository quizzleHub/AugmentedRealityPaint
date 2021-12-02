from PyQt5.QtGui import QColor
from CommandInterface import CommandInterface


class CmdSetStrokeColor(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = True
    def execute(self):
        self.view.grafikView.setStrokeColor(QColor(255,0,0))
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool
