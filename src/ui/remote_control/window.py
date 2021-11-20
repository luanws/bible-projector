from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_RemoteControlWindow(object):
    def setupUi(self, RemoteControlWindow):
        RemoteControlWindow.setObjectName("RemoteControlWindow")
        self.centralwidget = QtWidgets.QWidget(RemoteControlWindow)
        self.centralwidget.setObjectName("centralwidget")
        RemoteControlWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(RemoteControlWindow)
        QtCore.QMetaObject.connectSlotsByName(RemoteControlWindow)
    def retranslateUi(self, RemoteControlWindow):
        _translate = QtCore.QCoreApplication.translate
        RemoteControlWindow.setWindowTitle(_translate("RemoteControlWindow", "Controle remoto"))
