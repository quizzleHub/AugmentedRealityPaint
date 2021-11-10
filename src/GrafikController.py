
from GrafikView import GrafikView



class GrafikController:

    grafikView = None
    model = None

    
    def __init__(self, grafikView, model) -> None:
        self.grafikView = grafikView
        self.model = model
        
    def registerEvents(self):
        #view.getButton1().addActionListener(self)
        #view.getButton1().addActionListener(self)
        #view.getButton1().addActionListener(self)
        print("registered events in GrafikController")

    #def actionPerformed(event):
        #ggfs noch command design pattern oder switch case
