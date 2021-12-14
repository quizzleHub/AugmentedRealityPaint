from PyQt5.QtGui import QColor
from commands.CommandInterface import CommandInterface


class CmdSetStrokeColor(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = True
    def execute(self):
        self.view.grafikView.setStrokeColor(QColor(0,0,255))
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool
