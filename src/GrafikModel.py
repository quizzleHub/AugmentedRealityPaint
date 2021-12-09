from Figure import Figure

class GrafikModel():
    
    def __init__(self) -> None:
        self.figures = []
        #self.figures = [Figure]
    
    def addFigure(self):
        #create a new Figure and append to Figures-List
        self.figures.append(Figure())   

    def getFigures(self):
        return self.figures

    def addPoint(self, point):
        """addPoints gets called by CVModel when a new tracking coordinate is available"""
        #get last figure and add Point
        self.figures[-1].addPoint(point)



