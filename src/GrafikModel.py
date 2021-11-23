
class GrafikModel():
    
    def __init__(self) -> None:
        self.x = 3
        self.points = [] 
    
    def recPoint(self, point):
        self.points.append(point)
        print("gm: " + str(point))
