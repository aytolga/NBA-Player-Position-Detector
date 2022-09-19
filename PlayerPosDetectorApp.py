# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nba_player_pos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import pickle


def PosFinder(fg, ft, tp, trb, ast, blk,height,weigth):
    with open("model_pickle", "rb") as f:                     #Importing the last model
        clf = pickle.load(f)

    player = np.array([[fg, ft, tp, trb, ast, blk, height, weigth]])

    clf_player = clf.predict(player)

    return int(clf_player)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 8, 1, 1, 1)
        self.temizle = QtWidgets.QPushButton(self.centralwidget)
        self.temizle.setObjectName("temizle")
        self.gridLayout.addWidget(self.temizle, 9, 0, 1, 1)
        self.uygula = QtWidgets.QPushButton(self.centralwidget)
        self.uygula.setObjectName("uygula")
        self.gridLayout.addWidget(self.uygula, 9, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.sonuc = QtWidgets.QLabel("Sonuç Burada Gösterilecektir...")
        #self.sonuc.setObjectName("sonuc")
        self.gridLayout_2.addWidget(self.sonuc, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        self.temizle.clicked.connect(self.lineEdit.clear)
        self.temizle.clicked.connect(self.lineEdit_2.clear)
        self.temizle.clicked.connect(self.lineEdit_3.clear)
        self.temizle.clicked.connect(self.lineEdit_4.clear)
        self.temizle.clicked.connect(self.lineEdit_5.clear)
        self.temizle.clicked.connect(self.lineEdit_6.clear)
        self.temizle.clicked.connect(self.lineEdit_7.clear)
        self.temizle.clicked.connect(self.lineEdit_8.clear)
        self.temizle.clicked.connect(self.lineEdit_9.clear)
        self.uygula.clicked.connect(self.goster)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Basketbol Oyuncu Pozisyon Bulucu")
        self.label.setText(_translate("MainWindow", "NBA Oyuncu Pozisyon Belirleme Uygulaması"))
        self.label_4.setText(_translate("MainWindow", "FT Yüzdesi"))
        self.label_5.setText(_translate("MainWindow", "3P Yüzdesi"))
        self.label_6.setText(_translate("MainWindow", "Sezon Boyu Alınan Ribaund Sayısı"))
        self.label_7.setText(_translate("MainWindow", "Sezon Boyu Yapılan Asist Sayısı"))
        self.label_2.setText(_translate("MainWindow", "Oyuncu Adı"))
        self.label_3.setText(_translate("MainWindow", "FG Yüzdesi"))
        self.temizle.setText(_translate("MainWindow", "Temizle"))
        self.uygula.setText(_translate("MainWindow", "Uygula"))
        self.label_9.setText(_translate("MainWindow", "Oyuncunun Boyu (cm) "))
        self.label_10.setText(_translate("MainWindow", "Oyuncunun Kilosu (kg)"))
        self.label_8.setText(_translate("MainWindow", "Sezon Boyu Yapılan Blok Sayısı"))

    def goster(self):
        ad = self.lineEdit.text()
        fg = self.lineEdit_2.text()
        fg1 = float(fg)
        ft = self.lineEdit_3.text()
        ft1 = float(ft)
        tp = self.lineEdit_4.text()
        tp1 = float(tp)
        trb = self.lineEdit_5.text()
        trb1 = float(trb)
        ast = self.lineEdit_6.text()
        ast1 = float(ast)
        blk = self.lineEdit_7.text()         #The backend section coded by me (aytolga@outlook.com) other parts maden in QtDesigner.
        blk1 = float(blk)
        h = self.lineEdit_8.text()
        h1 = float(h)
        w = self.lineEdit_9.text()
        w1 = float(w)
        self.oyuncu = PosFinder(fg1,ft1,tp1,trb1,ast1,blk1,h1,w1)

        if self.oyuncu == 1:
            self.oyuncu = "PG"
        elif self.oyuncu == 2:
            self.oyuncu = "SG"
        elif self.oyuncu == 3:
            self.oyuncu = "SF"
        elif self.oyuncu == 4:
            self.oyuncu = "PF"
        elif self.oyuncu == 5:
            self.oyuncu = "C"

        self.sonuc.setText("Oyuncu Adı = {} \nPozisyon = {}".format(ad,self.oyuncu))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

