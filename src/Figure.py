
class Figure():

    def __init__(self) -> None:
        self.points = []        #list of points

    def addPoint(self, point):
        self.points.append(point)

    def getPoints(self):
        return self.points