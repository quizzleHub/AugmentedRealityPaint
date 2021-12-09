from Figure import Figure
from PyQt5.QtWidgets import QFileDialog

class GrafikModel():
    
    def __init__(self) -> None:
        self.figures = []
        #self.figures = [Figure]
    
    def addFigure(self):
        #create a new Figure and append to Figures-List
        self.figures.append(Figure())   
        print("New figure created")

    def getFigures(self):
        return self.figures

    def addPoint(self, point):
        #get last figure and add Point
        self.figures[-1].addPoint(point)
        print("Added point to figure")

    def recPoint(self, point):
        print("received point")
        self.addPoint(point)

    def safeFigures(self):
        dialog = QFileDialog()

        if dialog.exec_() == QFileDialog.Accepted:
            selectedfile = dialog.selectedFiles()
            file = open(str(selectedfile[0]), "w")

            for f in self.figures:
                file.write("Figure: " + str(f) + "\n")
                points = f.getPoints()
                for p in points:
                    file.write(str(p) + "\n")
                file.write("\n")
            file.close()

    def openFigures(self):

        dialog = QFileDialog()

        if dialog.exec_() == QFileDialog.Accepted:
            file = open(str(dialog.selectedFiles()), "r")

            # read file
            
            file.close()

        



