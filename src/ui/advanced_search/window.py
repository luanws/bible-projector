from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.versions_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.versions_combo_box.setObjectName("versions_combo_box")
        self.horizontalLayout.addWidget(self.versions_combo_box)
        self.search_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_line_edit.setObjectName("search_line_edit")
        self.horizontalLayout.addWidget(self.search_line_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.chapter_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.chapter_list_widget.setObjectName("chapter_list_widget")
        self.verticalLayout.addWidget(self.chapter_list_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pesquisa avançada"))
