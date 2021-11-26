# -*- coding: utf-8 -*-



# Neue View in Projekt einpflegen:
#   1. form.ui mit designer erstellen
#   2. pyuic5 -x form.ui -o form.py
#   3. Klassenname in "View" ändern
#   4. Alles nach und inklusive "if __name__ == "__main__": löschen
#   5. Getter für sämtliche Button/Labels/Objekte erstellen



from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path



class View(object):
    def setupUi(self, MainWindow):
        cwd = Path.cwd()
        rootdir = cwd.parent.absolute()
        iconsdir = rootdir/"icons"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1232, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1231, 721))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1232, 22))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuOptionen = QtWidgets.QMenu(self.menubar)
        self.menuOptionen.setObjectName("menuOptionen")
        self.menuZeichnen = QtWidgets.QMenu(self.menubar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(str(iconsdir/"zeichnen.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuZeichnen.setIcon(icon)
        self.menuZeichnen.setObjectName("menuZeichnen")
        self.menuRadieren = QtWidgets.QMenu(self.menubar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(str(iconsdir/"radierer.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRadieren.setIcon(icon1)
        self.menuRadieren.setObjectName("menuRadieren")
        self.menuFarbe = QtWidgets.QMenu(self.menubar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(str(iconsdir/"Farbe.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuFarbe.setIcon(icon2)
        self.menuFarbe.setObjectName("menuFarbe")
        self.menuStrickdicke = QtWidgets.QMenu(self.menubar)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(str(iconsdir/"Strickdicke.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuStrickdicke.setIcon(icon3)
        self.menuStrickdicke.setObjectName("menuStrickdicke")
        self.menuUndo = QtWidgets.QMenu(self.menubar)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(str(iconsdir/"undo.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuUndo.setIcon(icon4)
        self.menuUndo.setObjectName("menuUndo")
        self.menuRedo = QtWidgets.QMenu(self.menubar)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(str(iconsdir/"redo.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRedo.setIcon(icon5)
        self.menuRedo.setObjectName("menuRedo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNeu = QtWidgets.QAction(MainWindow)
        self.actionNeu.setObjectName("actionNeu")
        self.actionOeffnen = QtWidgets.QAction(MainWindow)
        self.actionOeffnen.setObjectName("actionOeffnen")
        self.actionSpeichern = QtWidgets.QAction(MainWindow)
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.actionExportieren = QtWidgets.QAction(MainWindow)
        self.actionExportieren.setObjectName("actionExportieren")
        self.actionKalibrieren = QtWidgets.QAction(MainWindow)
        self.actionKalibrieren.setObjectName("actionKalibrieren")
        self.actionHilfe = QtWidgets.QAction(MainWindow)
        self.actionHilfe.setObjectName("actionHilfe")
        self.actionrot = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(str(iconsdir/"rot.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionrot.setIcon(icon6)
        self.actionrot.setObjectName("actionrot")
        self.actiongruen = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(str(iconsdir/"gruen.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiongruen.setIcon(icon7)
        self.actiongruen.setObjectName("actiongruen")
        self.actionblau = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(str(iconsdir/"blau.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionblau.setIcon(icon8)
        self.actionblau.setObjectName("actionblau")
        self.actiongelb = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(str(iconsdir/"gelb.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiongelb.setIcon(icon9)
        self.actiongelb.setObjectName("actiongelb")
        self.actionweiss = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(str(iconsdir/"weiss.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionweiss.setIcon(icon10)
        self.actionweiss.setObjectName("actionweiss")
        self.actionDuenn = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(str(iconsdir/"duenn.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDuenn.setIcon(icon11)
        self.actionDuenn.setObjectName("actionDuenn")
        self.actionMittel = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(str(iconsdir/"mittel.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMittel.setIcon(icon12)
        self.actionMittel.setObjectName("actionMittel")
        self.actionDick = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(str(iconsdir/"dick.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDick.setIcon(icon13)
        self.actionDick.setObjectName("actionDick")
        self.actionschwarz = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(str(iconsdir/"schwarz.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionschwarz.setIcon(icon14)
        self.actionschwarz.setObjectName("actionschwarz")
        self.menuOptionen.addAction(self.actionNeu)
        self.menuOptionen.addAction(self.actionOeffnen)
        self.menuOptionen.addAction(self.actionSpeichern)
        self.menuOptionen.addAction(self.actionExportieren)
        self.menuOptionen.addAction(self.actionKalibrieren)
        self.menuOptionen.addAction(self.actionHilfe)
        self.menuFarbe.addAction(self.actionrot)
        self.menuFarbe.addAction(self.actiongruen)
        self.menuFarbe.addAction(self.actionblau)
        self.menuFarbe.addAction(self.actiongelb)
        self.menuFarbe.addAction(self.actionweiss)
        self.menuFarbe.addAction(self.actionschwarz)
        self.menuStrickdicke.addAction(self.actionDuenn)
        self.menuStrickdicke.addAction(self.actionMittel)
        self.menuStrickdicke.addAction(self.actionDick)
        self.menubar.addAction(self.menuOptionen.menuAction())
        self.menubar.addAction(self.menuZeichnen.menuAction())
        self.menubar.addAction(self.menuRadieren.menuAction())
        self.menubar.addAction(self.menuFarbe.menuAction())
        self.menubar.addAction(self.menuStrickdicke.menuAction())
        self.menubar.addAction(self.menuUndo.menuAction())
        self.menubar.addAction(self.menuRedo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuOptionen.setTitle(_translate("MainWindow", "Optionen"))
        self.menuZeichnen.setTitle(_translate("MainWindow", "Zeichnen"))
        self.menuRadieren.setTitle(_translate("MainWindow", "Radieren"))
        self.menuFarbe.setTitle(_translate("MainWindow", "Farbe"))
        self.menuStrickdicke.setTitle(_translate("MainWindow", "Strickdicke"))
        self.menuUndo.setTitle(_translate("MainWindow", "Undo"))
        self.menuRedo.setTitle(_translate("MainWindow", "Redo"))
        self.actionNeu.setText(_translate("MainWindow", "Neu"))
        self.actionOeffnen.setText(_translate("MainWindow", "Öffnen"))
        self.actionSpeichern.setText(_translate("MainWindow", "Speichern"))
        self.actionExportieren.setText(_translate("MainWindow", "Exportieren"))
        self.actionKalibrieren.setText(_translate("MainWindow", "Kalibrieren"))
        self.actionHilfe.setText(_translate("MainWindow", "Hilfe"))
        self.actionrot.setText(_translate("MainWindow", "rot"))
        self.actiongruen.setText(_translate("MainWindow", "grün"))
        self.actiongruen.setToolTip(_translate("MainWindow", "grün"))
        self.actionblau.setText(_translate("MainWindow", "blau"))
        self.actiongelb.setText(_translate("MainWindow", "gelb"))
        self.actionweiss.setText(_translate("MainWindow", "weiß"))
        self.actionDuenn.setText(_translate("MainWindow", "Dünn"))
        self.actionMittel.setText(_translate("MainWindow", "Mittel"))
        self.actionDick.setText(_translate("MainWindow", "Dick"))
        self.actionschwarz.setText(_translate("MainWindow", "schwarz"))

# -------------------------------------Getter---------------------------

    def getbtnOptionen(self):
        return self.menuOptionen

    def getbtnNeu(self):
        return self.actionNeu

    def getbtnOeffnen(self):
        return self.actionOeffnen

    def getbtnSpeichern(self):
        return self.actionSpeichern

    def getbtnExportieren(self):
        return self.actionExportieren

    def getbtnKalibrieren(self):
        return self.actionKalibrieren

    def getbtnHilfe(self):
        return self.actionHilfe

    def getbtnZeichnen(self):
        return self.menuZeichnen

    def getbtnRadieren(self):
        return self.menuRadieren

    def getbtnFarbe(self):
        return self.menuFarbe

    def getbtnRot(self):
        return self.actionrot

    def getbtnGruen(self):
        return self.actiongruen

    def getbtnBlau(self):
        return self.actionblau

    def getbtnGelb(self):
        return self.actiongelb

    def getbtnWeiss(self):
        return self.actionweiss

    def getbtnSchwarz(self):
        return self.actionschwarz

    def getbtnStrickdicke(self):
        return self.menuStrickdicke

    def getbtnDick(self):
        return self.actionDick

    def getbtnMittel(self):
        return self.actionMittel

    def getbtnDuenn(self):
        return self.actionDuenn

    def getbtnUndo(self):
        return self.menuUndo

    def getbtnRedo(self):
        return self.menuRedo
    
    def getgraphicsView(self):
        return self.graphicsView


