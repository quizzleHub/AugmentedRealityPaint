from PyQt5 import QtGui

class GrafikAdapter:
    #https://www.pythonguis.com/tutorials/bitmap-graphics/

    def __init__(self, grafikView, grafikModel):
        self.grafikView = grafikView
        self.grafikModel = grafikModel
 
    #holt sich figuren aus GrafikModel und gibt sie an grafikView
    #grafikmodel pubsliher , grafikAdapter subscriber


    def recCamImg(self,camImg):
        self.grafikView.showImg(camImg)
        