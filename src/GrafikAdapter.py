

class GrafikAdapter:
    


    def __init__(self, grafikView, grafikModel) -> None:
        self.grafikView = grafikView
        self.grafikModel = grafikModel


    def recCamImg(self,camImg):
        self.grafikView.showImg(camImg)
        