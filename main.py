"""import sys
import time 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


starttime = time.time()
def main():
    global window,label,app
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(0, 0,400,400)
    window.setWindowTitle("Cing Checker")
    label = QtWidgets.QLabel(window)
    label.setText("Ahoj")
    label.move(50,50)
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()


#    label.setText(str(time.time()-starttime))
#    window.show()

"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connect_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.connect_BTN.setGeometry(QtCore.QRect(330, 370, 161, 61))
        self.connect_BTN.setObjectName("connect_BTN")
        self.heading_label = QtWidgets.QLabel(self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(380, 70, 49, 16))
        self.heading_label.setObjectName("heading_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connect_BTN.setText(_translate("MainWindow", "Connect"))
        self.heading_label.setText(_translate("MainWindow", "Cing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    