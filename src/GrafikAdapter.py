

from PyQt5 import QtGui


class GrafikAdapter:
    #https://www.pythonguis.com/tutorials/bitmap-graphics/


    def __init__(self, grafikView, grafikModel):
        self.grafikView = grafikView
        self.grafikModel = grafikModel
 
 


    def recCamImg(self,camImg):
        self.grafikView.showImg(camImg)
        