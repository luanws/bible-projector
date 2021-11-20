from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_RemoteControlWindow(object):
    def setupUi(self, RemoteControlWindow):
        RemoteControlWindow.setObjectName("RemoteControlWindow")
        self.centralwidget = QtWidgets.QWidget(RemoteControlWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.qr_code_label = QtWidgets.QLabel(self.centralwidget)
        self.qr_code_label.setText("")
        self.qr_code_label.setObjectName("qr_code_label")
        self.gridLayout.addWidget(self.qr_code_label, 0, 0, 1, 1)
        RemoteControlWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(RemoteControlWindow)
        QtCore.QMetaObject.connectSlotsByName(RemoteControlWindow)
    def retranslateUi(self, RemoteControlWindow):
        _translate = QtCore.QCoreApplication.translate
        RemoteControlWindow.setWindowTitle(_translate("RemoteControlWindow", "Controle remoto"))
