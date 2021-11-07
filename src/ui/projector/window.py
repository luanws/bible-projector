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
        self.textLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLabel.setStyleSheet("* {\n"
"    font: 8pt \"Berlin Sans FB\";\n"
"    color: white;\n"
"    font-size: 30px;\n"
"    margin: 50%;\n"
"}")
        self.textLabel.setTextFormat(QtCore.Qt.AutoText)
        self.textLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.textLabel.setWordWrap(True)
        self.textLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textLabel.setObjectName("textLabel")
        self.gridLayout.addWidget(self.textLabel, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projetor"))
        self.textLabel.setText(_translate("MainWindow", "Texto bíblico"))
