# -*- coding: utf-8 -*-



# Neue View in Projekt einpflegen:
#   1. form.ui mit designer erstellen
#   2. pyuic5 -x form.ui -o form.py
#   3. Klassenname in "View" ändern
#   4. Alles nach und inklusive "if __name__ == "__main__": löschen
#   5. Getter für sämtliche Button/Labels/Objekte erstellen


from PyQt5 import QtCore, QtGui, QtWidgets


class View(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAction = QtWidgets.QPushButton(self.centralwidget)
        self.btnAction.setGeometry(QtCore.QRect(210, 380, 113, 32))
        self.btnAction.setObjectName("Action")
        self.btnUndo = QtWidgets.QPushButton(self.centralwidget)
        self.btnUndo.setGeometry(QtCore.QRect(310, 380, 113, 32))
        self.btnUndo.setObjectName("Undo")
        self.btnRedo = QtWidgets.QPushButton(self.centralwidget)
        self.btnRedo.setGeometry(QtCore.QRect(410, 380, 113, 32))
        self.btnRedo.setObjectName("Undo")
        self.lblLabel = QtWidgets.QLabel(self.centralwidget)
        self.lblLabel.setGeometry(QtCore.QRect(210, 200, 400, 16))
        self.lblLabel.setObjectName("Label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAction.setText(_translate("MainWindow", "Action"))
        self.btnUndo.setText(_translate("MainWindow", "Undo"))
        self.btnRedo.setText(_translate("MainWindow", "Redo"))
        self.lblLabel.setText(_translate("MainWindow", "Trial Version AugmentedRealityPaint"))


#___________Getter_________________
    def getbtnAction(self):
        return self.btnAction

    def getbtnUndo(self):
        return self.btnUndo

    def getbtnRedo(self):
        return self.btnRedo

    def getlblLabel(self):
        return self.lblLabel


