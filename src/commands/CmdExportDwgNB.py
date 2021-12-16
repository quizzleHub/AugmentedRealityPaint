from commands.CommandInterface import CommandInterface

class CmdExportDrawingNB(CommandInterface):

    def __init__(self, view, graphicsModel, cvModel):
        self.view = view                
        self.graphicsModel = graphicsModel
        self.cvModel = cvModel
        self.isUndoableBool = False
    def execute(self, *args):
        print("ExportDrawingNB executed")
        qImage = self.view.graphicsView.drawImage(self.cvModel.getWidth(), self.cvModel.getHeight())
        self.graphicsModel.exportDrawing(qImage)
    def redo(self):
        print("Action redone")
    def undo(self):
        print("Action undone")
    def isUndoable(self):
        return self.isUndoableBool
