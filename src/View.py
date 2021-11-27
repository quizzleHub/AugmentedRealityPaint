# -*- coding: utf-8 -*-


# Verändern falls neue .ui Datei:
#   1. Pfad für icons erstellen :
#         cwd = Path.cwd()
#         rootdir = cwd.parent.absolute()
#         iconsdir = rootdir / "icons"
#   2. Pfade anpassen mit (str(iconsdir/"Bildname.PNG"))
#   3. Getter einfügen
#----------------------------------------------------------
# Neue View in Projekt einpflegen:
#   1. form.ui mit designer erstellen
#   2. pyuic5 -x form.ui -o form.py
#   3. Klassenname in "View" ändern
#   4. Alles nach und inklusive "if __name__ == "__main__": löschen

from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path

class View(object):
    def setupUi(self, View):
        cwd = Path.cwd()
        rootdir = cwd.parent.absolute()
        iconsdir = rootdir / "icons"
        View.setObjectName("View")
        View.resize(1232, 768)
        self.centralwidget = QtWidgets.QWidget(View)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QLabel(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1231, 721))
        self.graphicsView.setObjectName("graphicsView")
        View.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(View)
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
        self.menuStrichdicke = QtWidgets.QMenu(self.menubar)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(str(iconsdir / "Strichdicke.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuStrichdicke.setIcon(icon3)
        self.menuStrichdicke.setObjectName("menuStrichdicke")
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
        View.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(View)
        self.statusbar.setObjectName("statusbar")
        View.setStatusBar(self.statusbar)
        self.actionNeu = QtWidgets.QAction(View)
        self.actionNeu.setObjectName("actionNeu")
        self.actionOeffnen = QtWidgets.QAction(View)
        self.actionOeffnen.setObjectName("actionOeffnen")
        self.actionSpeichern = QtWidgets.QAction(View)
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.actionExportieren = QtWidgets.QAction(View)
        self.actionExportieren.setObjectName("actionExportieren")
        self.actionKalibrieren = QtWidgets.QAction(View)
        self.actionKalibrieren.setObjectName("actionKalibrieren")
        self.actionHilfe = QtWidgets.QAction(View)
        self.actionHilfe.setObjectName("actionHilfe")
        self.actionrot = QtWidgets.QAction(View)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(str(iconsdir/"rot.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionrot.setIcon(icon6)
        self.actionrot.setObjectName("actionrot")
        self.actiongruen = QtWidgets.QAction(View)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(str(iconsdir/"gruen.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiongruen.setIcon(icon7)
        self.actiongruen.setObjectName("actiongruen")
        self.actionblau = QtWidgets.QAction(View)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(str(iconsdir/"blau.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionblau.setIcon(icon8)
        self.actionblau.setObjectName("actionblau")
        self.actiongelb = QtWidgets.QAction(View)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(str(iconsdir/"gelb.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiongelb.setIcon(icon9)
        self.actiongelb.setObjectName("actiongelb")
        self.actionweiss = QtWidgets.QAction(View)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(str(iconsdir/"weiss.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionweiss.setIcon(icon10)
        self.actionweiss.setObjectName("actionweiss")
        self.actionDuenn = QtWidgets.QAction(View)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(str(iconsdir/"duenn.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDuenn.setIcon(icon11)
        self.actionDuenn.setObjectName("actionDuenn")
        self.actionMittel = QtWidgets.QAction(View)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(str(iconsdir/"mittel.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMittel.setIcon(icon12)
        self.actionMittel.setObjectName("actionMittel")
        self.actionDick = QtWidgets.QAction(View)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(str(iconsdir/"dick.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDick.setIcon(icon13)
        self.actionDick.setObjectName("actionDick")
        self.actionschwarz = QtWidgets.QAction(View)
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
        self.menuStrichdicke.addAction(self.actionDuenn)
        self.menuStrichdicke.addAction(self.actionMittel)
        self.menuStrichdicke.addAction(self.actionDick)
        self.menubar.addAction(self.menuOptionen.menuAction())
        self.menubar.addAction(self.menuZeichnen.menuAction())
        self.menubar.addAction(self.menuRadieren.menuAction())
        self.menubar.addAction(self.menuFarbe.menuAction())
        self.menubar.addAction(self.menuStrichdicke.menuAction())
        self.menubar.addAction(self.menuUndo.menuAction())
        self.menubar.addAction(self.menuRedo.menuAction())

        self.retranslateUi(View)
        QtCore.QMetaObject.connectSlotsByName(View)

    def retranslateUi(self, View):
        _translate = QtCore.QCoreApplication.translate
        View.setWindowTitle(_translate("View", "View"))
        self.menuOptionen.setTitle(_translate("View", "Optionen"))
        self.menuZeichnen.setTitle(_translate("View", "Zeichnen"))
        self.menuRadieren.setTitle(_translate("View", "Radieren"))
        self.menuFarbe.setTitle(_translate("View", "Farbe"))
        self.menuStrichdicke.setTitle(_translate("View", "Strichdicke"))
        self.menuUndo.setTitle(_translate("View", "Undo"))
        self.menuRedo.setTitle(_translate("View", "Redo"))
        self.actionNeu.setText(_translate("View", "Neu"))
        self.actionOeffnen.setText(_translate("View", "Öffnen"))
        self.actionSpeichern.setText(_translate("View", "Speichern"))
        self.actionExportieren.setText(_translate("View", "Exportieren"))
        self.actionKalibrieren.setText(_translate("View", "Kalibrieren"))
        self.actionHilfe.setText(_translate("View", "Hilfe"))
        self.actionrot.setText(_translate("View", "rot"))
        self.actiongruen.setText(_translate("View", "grün"))
        self.actiongruen.setToolTip(_translate("View", "grün"))
        self.actionblau.setText(_translate("View", "blau"))
        self.actiongelb.setText(_translate("View", "gelb"))
        self.actionweiss.setText(_translate("View", "weiß"))
        self.actionDuenn.setText(_translate("View", "Dünn"))
        self.actionMittel.setText(_translate("View", "Mittel"))
        self.actionDick.setText(_translate("View", "Dick"))
        self.actionschwarz.setText(_translate("View", "schwarz"))

# -------------------------------------Getter---------------------------
    def getGraphicsView(self):
        return self.graphicsView

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

    def getbtnStrichdicke(self):
        return self.menuStrichdicke

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


