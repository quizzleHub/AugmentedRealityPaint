from commands.CommandInterface import CommandInterface


class CmdExportDrawingNB(CommandInterface):

    def __init__(self, view, graphicsModel, cvModel):
        self.view = view                
        self.graphicsModel = graphicsModel
        self.cvModel = cvModel
        self.isUndoableBool = False

    def execute(self, *args):
        qImage = self.view.graphicsView.drawImage(self.cvModel.getWidth(), self.cvModel.getHeight())
        self.graphicsModel.exportDrawing(qImage)

    def redo(self):
        pass

    def undo(self):
        pass
    
    def isUndoable(self):
        return self.isUndoableBool
