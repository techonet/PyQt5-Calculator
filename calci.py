# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calci.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.S1 = ""
        self.S2 = ""
        self.S3 = ""
        self.S4 = ""
        self.S5 = ""
        self.S6 = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(150, 80, 80, 23))
        self.B1.setObjectName("B1")
        self.B1.clicked.connect(self.B1change)
        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(250, 80, 80, 23))
        self.B2.setObjectName("B2")
        self.B2.clicked.connect(self.B2change)
        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(350, 80, 80, 23))
        self.B3.setObjectName("B3")
        self.B3.clicked.connect(self.B3change)
        self.B4 = QtWidgets.QPushButton(self.centralwidget)
        self.B4.setGeometry(QtCore.QRect(150, 110, 80, 23))
        self.B4.setObjectName("B4")
        self.B4.clicked.connect(self.B4change)
        self.B5 = QtWidgets.QPushButton(self.centralwidget)
        self.B5.setGeometry(QtCore.QRect(250, 110, 80, 23))
        self.B5.setObjectName("B5")
        self.B5.clicked.connect(self.B5change)
        self.B6 = QtWidgets.QPushButton(self.centralwidget)
        self.B6.setGeometry(QtCore.QRect(350, 110, 80, 23))
        self.B6.setObjectName("B6")
        self.B6.clicked.connect(self.B6change)
        self.B7 = QtWidgets.QPushButton(self.centralwidget)
        self.B7.setGeometry(QtCore.QRect(150, 140, 80, 23))
        self.B7.setObjectName("B7")
        self.B7.clicked.connect(self.B7change)
        self.B8 = QtWidgets.QPushButton(self.centralwidget)
        self.B8.setGeometry(QtCore.QRect(250, 140, 80, 23))
        self.B8.setObjectName("B8")
        self.B8.clicked.connect(self.B8change)
        self.B9 = QtWidgets.QPushButton(self.centralwidget)
        self.B9.setGeometry(QtCore.QRect(350, 140, 80, 23))
        self.B9.setObjectName("B9")
        self.B9.clicked.connect(self.B9change)
        self.B10 = QtWidgets.QPushButton(self.centralwidget)
        self.B10.setGeometry(QtCore.QRect(150, 170, 80, 23))
        self.B10.setObjectName("B10")
        self.B10.clicked.connect(self.B10change)
        self.B11 = QtWidgets.QPushButton(self.centralwidget)
        self.B11.setGeometry(QtCore.QRect(250, 170, 80, 23))
        self.B11.setObjectName("B11")
        self.B11.clicked.connect(self.B11change)
        self.B12 = QtWidgets.QPushButton(self.centralwidget)
        self.B12.setGeometry(QtCore.QRect(350, 170, 80, 23))
        self.B12.setObjectName("B12")
        self.B12.clicked.connect(self.B12change)
        self.B13 = QtWidgets.QPushButton(self.centralwidget)
        self.B13.setGeometry(QtCore.QRect(450, 80, 80, 23))
        self.B13.setObjectName("B13")
        self.B13.clicked.connect(self.B13change)
        self.B14 = QtWidgets.QPushButton(self.centralwidget)
        self.B14.setGeometry(QtCore.QRect(450, 110, 80, 23))
        self.B14.setObjectName("B14")
        self.B14.clicked.connect(self.B14change)
        self.B15 = QtWidgets.QPushButton(self.centralwidget)
        self.B15.setGeometry(QtCore.QRect(450, 140, 80, 23))
        self.B15.setObjectName("B15")
        self.B15.clicked.connect(self.B15change)
        self.B16 = QtWidgets.QPushButton(self.centralwidget)
        self.B16.setGeometry(QtCore.QRect(450, 170, 80, 23))
        self.B16.setObjectName("B16")
        self.B16.clicked.connect(self.B16change)
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(150, 42, 381, 21))
        self.T1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T1.setObjectName("T1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 20))
        self.menubar.setObjectName("menubar")
        self.menuhOME = QtWidgets.QMenu(self.menubar)
        self.menuhOME.setObjectName("menuhOME")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuhOME.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.B1.setText(_translate("MainWindow", "1"))
        self.B2.setText(_translate("MainWindow", "2"))
        self.B3.setText(_translate("MainWindow", "3"))
        self.B4.setText(_translate("MainWindow", "4"))
        self.B5.setText(_translate("MainWindow", "5"))
        self.B6.setText(_translate("MainWindow", "6"))
        self.B7.setText(_translate("MainWindow", "7"))
        self.B8.setText(_translate("MainWindow", "8"))
        self.B9.setText(_translate("MainWindow", "9"))
        self.B10.setText(_translate("MainWindow", "0"))
        self.B11.setText(_translate("MainWindow", "CLS"))
        self.B12.setText(_translate("MainWindow", "="))
        self.B13.setText(_translate("MainWindow", "+"))
        self.B14.setText(_translate("MainWindow", "-"))
        self.B15.setText(_translate("MainWindow", "*"))
        self.B16.setText(_translate("MainWindow", "/"))
        self.T1.setText(_translate("MainWindow", "0"))
        self.menuhOME.setTitle(_translate("MainWindow", "Home"))
        
    def B1change(self):
        C1 = str(self.T1.text())
        C2 = str(self.B1.text())
        C3 = C1 + C2
        self.T1.setText(C3)
   
    def B2change(self):
        C1 = str(self.T1.text())
        C2 = str(self.B2.text())
        C3 = C1 + C2
        self.T1.setText(C3)
    
    def B3change(self):
        C1 = str(self.T1.text())
        C2 = str(self.B3.text())
        C3 = C1 + C2
        self.T1.setText(C3)
    
    def B4change(self):
        C1 = str(self.T1.text())
        C2 = str(self.B4.text())
        C3 = C1 + C2
        self.T1.setText(C3)
    
    def B5change(self):
        C1 = str(self.T1.text())
        C2 = str(self.B5.text())
        C3 = C1 + C2
        self.T1.setText(C3)
    
    def B6change(self):
        C1 = str(self.T1.text())
        C2 = str(self.B6.text())
        C3 = C1 + C2
        self.T1.setText(C3)
    
    def B7change(self):
        C1 = str(self.T1.text())
        C2 = str(self.B7.text())
        C3 = C1 + C2
        self.T1.setText(C3)
    
    def B8change(self):
        C1 = str(self.T1.text())
        C2 = str(self.B8.text())
        C3 = C1 + C2
        self.T1.setText(C3)
    
    def B9change(self):
        C1 = str(self.T1.text())
        C2 = str(self.B9.text())
        C3 = C1 + C2
        self.T1.setText(C3)
    
    def B10change(self):
        C1 = str(self.T1.text())
        C2 = str(self.B10.text())
        C3 = C1 + C2
        self.T1.setText(C3)
    
    def B11change(self):
        self.T1.setText("")
    
    def B12change(self):
        self.S3 = str(self.T1.text())
        if(self.S2 == "+"):
            I1 = int(self.S1) + int(self.S3)
        elif(self.S2 == "-"):
            I1 = int(self.S1) - int(self.S3)
        elif(self.S2 == "*"):
            I1 = int(self.S1) * int(self.S3)
        elif(self.S2 == "/"):
            I1 = int(self.S1) / int(self.S3)
        else:
            I1 = ""
        self.T1.setText(str(I1))
    
    def B13change(self):
        self.S1 = str(self.T1.text())
        self.T1.setText("")
        self.S2 = "+"
    
    def B14change(self):
        self.S1 = str(self.T1.text())
        self.T1.setText("")
        self.S2 = "-"
    
    def B15change(self):
        self.S1 = str(self.T1.text())
        self.T1.setText("")
        self.S2 = "*"
    
    def B16change(self):
        self.S1 = str(self.T1.text())
        self.T1.setText("")
        self.S2 = "/"



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
