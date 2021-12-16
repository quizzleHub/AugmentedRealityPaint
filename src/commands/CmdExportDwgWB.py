from commands.CommandInterface import CommandInterface

class CmdExportDrawingWB(CommandInterface):

    def __init__(self, view, graphicsModel, cvModel):
        self.view = view                
        self.graphicsModel = graphicsModel
        self.cvModel = cvModel
        self.isUndoableBool = False
    def execute(self, *args):
        print("ExportDrawingWB executed")
        qImage = self.view.graphicsView.getScaledImage()
        self.graphicsModel.exportDrawing(qImage)
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool
