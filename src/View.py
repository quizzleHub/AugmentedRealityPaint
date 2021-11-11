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
        self.btnButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnButton1.setGeometry(QtCore.QRect(210, 380, 113, 32))
        self.btnButton1.setObjectName("btnButton1")
        self.btnButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnButton2.setGeometry(QtCore.QRect(510, 380, 113, 32))
        self.btnButton2.setObjectName("btnButton2")
        self.lblLabel = QtWidgets.QLabel(self.centralwidget)
        self.lblLabel.setGeometry(QtCore.QRect(300, 200, 60, 16))
        self.lblLabel.setObjectName("lblLabel")
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
        self.btnButton1.setText(_translate("MainWindow", "PushButton"))
        self.btnButton2.setText(_translate("MainWindow", "PushButton"))
        self.lblLabel.setText(_translate("MainWindow", "TextLabel"))


#___________Getter_________________
    def getbtnButton1(self):
        return self.btnButton1

    def getbtnButton2(self):
        return self.btnButton2

    def getlblLabel(self):
        return self.lblLabel


