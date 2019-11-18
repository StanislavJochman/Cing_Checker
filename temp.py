# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToolBar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import time

from PyQt5 import QtCore, QtGui, QtWidgets

starttime = time.time()
def gettime():
    return time.time()-starttime
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(338, 185, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menuPort = QtWidgets.QMenu(self.menubar)
        self.menuPort.setObjectName("menuPort")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCOM1 = QtWidgets.QAction(MainWindow)
        self.actionCOM1.setObjectName("actionCOM1")
        self.actionCOM2 = QtWidgets.QAction(MainWindow)
        self.actionCOM2.setObjectName("actionCOM2")
        self.actionCOM0 = QtWidgets.QAction(MainWindow)
        self.actionCOM0.setObjectName("actionCOM0")
        self.menuPort.addSeparator()
        self.menuPort.addAction(self.actionCOM0)
        self.menuPort.addAction(self.actionCOM1)
        self.menuPort.addAction(self.actionCOM2)
        self.menubar.addAction(self.menuPort.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionCOM0.triggered.connect(lambda: self.clicked(str(gettime())))
        self.actionCOM1.triggered.connect(lambda: self.clicked("COM1"))
        self.actionCOM2.triggered.connect(lambda: self.clicked("COM2"))

        QtCore.QTimer.singleShot(10, self.getSensorValue)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Text"))
        self.menuPort.setTitle(_translate("MainWindow", "Port"))
        self.actionCOM1.setText(_translate("MainWindow", "COM1"))
        self.actionCOM2.setText(_translate("MainWindow", "COM2"))
        self.actionCOM0.setText(_translate("MainWindow", "COM0"))

    def clicked(self, text):
            self.label.setText(text)
            self.label.adjustSize()
    def updateValue(self,text):
            print(text)
            #label.setText(text)
            #label.adjustSize()
    def getSensorValue(self):
        print(gettime())
        self.label.setText(str(round(gettime(),1)))
        self.label.adjustSize()
        QtCore.QTimer.singleShot(10, self.getSensorValue)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.updateValue(gettime())
    MainWindow.show()
    sys.exit(app.exec_())
