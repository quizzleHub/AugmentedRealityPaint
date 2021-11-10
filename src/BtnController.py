
from View import View


class BtnController:

    view = None
    model = None

    
    def __init__(self, view, model) -> None:
        self.view = view
        self.model = model
        
    def registerEvents(self):
        btn1 = self.view.getbtnButton1()
        btn2 = self.view.getbtnButton2()
        label = self.view.getlblLabel()
        #view.getButton1().addActionListener(self)
        #view.getButton1().addActionListener(self)
        print("registered events in BtnController")

    #def actionPerformed(event):
        #ggfs noch command design pattern oder switch case

