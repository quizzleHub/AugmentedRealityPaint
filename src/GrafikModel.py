from Figure import Figure

class GrafikModel():
    
    def __init__(self) -> None:
        #self.figures = []
        self.figures = [Figure]
    
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
        print(self.figures[-1].__name__)

    # receive Point from CVModel, add new Figure and add Point to Figure
    def recPoint(self, point):
        #self.addFigure(self) # so wird jedesmal eine neue Figur erzeugt -> Falsch
        self.addPoint(point)

