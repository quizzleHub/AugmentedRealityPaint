# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Colorpicker(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Colorpicker ")

        # setting geometry
        self.setGeometry(100, 100, 500, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for components
    def UiComponents(self):
        # opening color dialog
        color = QColorDialog.getColor()

        # creating label to display the color
        label = QLabel(self)

        # setting geometry to the label
        label.setGeometry(100, 100, 200, 60)

        # making label multi line
        label.setWordWrap(True)

        # setting text to the label
        label.setText(str(color))

        # setting graphic effect to the label
        graphic = QGraphicsColorizeEffect(self)

        # setting color to the graphic
        graphic.setColor(color)

        # setting graphic to the label
        label.setGraphicsEffect(graphic)


App = QApplication(sys.argv)
window = Colorpicker()
sys.exit(App.exec())