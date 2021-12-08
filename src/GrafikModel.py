from Figure import Figure
import tkinter.filedialog

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

    # receive Point from CVModel, add new Figure and add Point to Figure
    def recPoint(self, point):
        #self.addFigure(self) # so wird jedesmal eine neue Figur erzeugt -> Falsch
        print("received point")
        self.addPoint(point)

    def safeFigures(self):
        filename = tkinter.filedialog.askopenfilename()
        file = open(filename, "w")

        for f in self.figures:
            file.write("Figure: " + f + "\n")
            points = f.getPoints()
            for p in points:
                file.write(p + "\n")
            file.write("\n")
        file.close()


        



