from commands.CommandInterface import CommandInterface


class CmdSetStrokeColor(CommandInterface):

    def __init__(self, view, model):
        self.view = view                
        self.model = model
        self.isUndoableBool = False

    def execute(self, *args):
        self.view.graphicsView.setStrokeColor(args[0]) 

        if args[1] == self.view.getbtnRed():
            self.view.getbtnBlue().setChecked(False)
            self.view.getbtnYellow().setChecked(False)

        if args[1] == self.view.getbtnBlue():
            self.view.getbtnRed().setChecked(False)
            self.view.getbtnYellow().setChecked(False)

        if args[1] == self.view.getbtnYellow():
            self.view.getbtnBlue().setChecked(False)
            self.view.getbtnRed().setChecked(False)

        if args[1] == self.view.getbtnColorPicker():
            self.view.getbtnRed().setChecked(False)
            self.view.getbtnBlue().setChecked(False)
            self.view.getbtnYellow().setChecked(False)
            
    def redo(self):
        pass

    def undo(self):
        pass

    def isUndoable(self):
        return self.isUndoableBool
        