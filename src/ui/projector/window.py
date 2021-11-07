from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 370)
        MainWindow.setStyleSheet("* {\n"
"    background-color: black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.text_label = QtWidgets.QLabel(self.centralwidget)
        self.text_label.setStyleSheet("* {\n"
"    font: 8pt \"Berlin Sans FB\";\n"
"    color: white;\n"
"    font-size: 30px;\n"
"    margin: 50%;\n"
"}")
        self.text_label.setTextFormat(QtCore.Qt.AutoText)
        self.text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.text_label.setWordWrap(True)
        self.text_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.text_label.setObjectName("text_label")
        self.gridLayout.addWidget(self.text_label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projetor"))
        self.text_label.setText(_translate("MainWindow", "Texto bíblico"))
