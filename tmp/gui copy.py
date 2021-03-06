# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(70, 40, 100, 100))
        self.pushButton_1.setStyleSheet(
            "border-image : url(images/dice1.png);")
        self.pushButton_1.setText("")
        self.pushButton_1.setCheckable(True)
        self.pushButton_1.setObjectName("pushButton")
        self.pushButton_1.clicked.connect(self.btnstate)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 40, 100, 100))
        self.pushButton_2.setStyleSheet(
            "border-image : url(images/dice2.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.btnstate)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 40, 100, 100))
        self.pushButton_3.setStyleSheet(
            "border-image : url(images/dice3.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.btnstate)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 40, 100, 100))
        self.pushButton_4.setStyleSheet(
            "border-image : url(images/dice4.png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.btnstate)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 40, 100, 100))
        self.pushButton_5.setStyleSheet(
            "border-image : url(images/dice5.png);")
        self.pushButton_5.setText("")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.btnstate)

        # bt lancer
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 190, 381, 61))
        self.pushButton_6.setObjectName("pushButton_6")

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(50, 290, 256, 192))
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(370, 290, 256, 192))
        self.tableView_2.setObjectName("tableView_2")
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
        self.pushButton_6.setText(_translate("MainWindow", "Lancer"))

    def btnstate(self):
        if self.pushButton_1.isChecked():
            self.pushButton_1.setStyleSheet("border-image : url(images/dice1_red.png);")
        else:
            self.pushButton_1.setStyleSheet("border-image : url(images/dice1.png);")

        if self.pushButton_2.isChecked():
            self.pushButton_2.setStyleSheet("border-image : url(images/dice2_red.png);")
        else:
            self.pushButton_2.setStyleSheet("border-image : url(images/dice2.png);")

        if self.pushButton_3.isChecked():
            self.pushButton_3.setStyleSheet("border-image : url(images/dice3_red.png);")
        else:
            self.pushButton_3.setStyleSheet("border-image : url(images/dice3.png);")

        if self.pushButton_4.isChecked():
            self.pushButton_4.setStyleSheet("border-image : url(images/dice4_red.png);")
        else:
            self.pushButton_4.setStyleSheet("border-image : url(images/dice4.png);")

        if self.pushButton_5.isChecked():
            self.pushButton_5.setStyleSheet("border-image : url(images/dice5_red.png);")
        else:
            self.pushButton_5.setStyleSheet("border-image : url(images/dice5.png);")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
