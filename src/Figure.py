
class Figure():

    def __init__(self) -> None:
        self.points = []        #list of points
        # strokeWidth: float
        # strokeColor: QColor

    def addPoint(self, point):
        self.points.append(point)

    def getPoints(self):
        return self.points