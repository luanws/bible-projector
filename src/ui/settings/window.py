from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
"    padding: 0px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 269))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preview_text_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.preview_text_line_edit.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.preview_text_line_edit.setPlaceholderText("")
        self.preview_text_line_edit.setObjectName("preview_text_line_edit")
        self.horizontalLayout.addWidget(self.preview_text_line_edit)
        self.font_family_combo_box = QtWidgets.QFontComboBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font_family_combo_box.sizePolicy().hasHeightForWidth())
        self.font_family_combo_box.setSizePolicy(sizePolicy)
        self.font_family_combo_box.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.font_family_combo_box.setObjectName("font_family_combo_box")
        self.horizontalLayout.addWidget(self.font_family_combo_box)
        self.font_size_spin_box = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font_size_spin_box.sizePolicy().hasHeightForWidth())
        self.font_size_spin_box.setSizePolicy(sizePolicy)
        self.font_size_spin_box.setMinimumSize(QtCore.QSize(50, 0))
        self.font_size_spin_box.setMaximumSize(QtCore.QSize(50, 16777215))
        self.font_size_spin_box.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.font_size_spin_box.setObjectName("font_size_spin_box")
        self.horizontalLayout.addWidget(self.font_size_spin_box)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(25, 0))
        self.label_3.setMaximumSize(QtCore.QSize(25, 16777215))
        self.label_3.setStyleSheet("* {\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;\n"
"    background-color: white;\n"
"}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.view_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_button.sizePolicy().hasHeightForWidth())
        self.view_button.setSizePolicy(sizePolicy)
        self.view_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.view_button.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 4px;\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"}\n"
"\n"
"*:hover {\n"
"    background-color: gray;\n"
"    color: white;\n"
"}")
        self.view_button.setObjectName("view_button")
        self.horizontalLayout.addWidget(self.view_button)
        self.apply_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_button.sizePolicy().hasHeightForWidth())
        self.apply_button.setSizePolicy(sizePolicy)
        self.apply_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.apply_button.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 4px;\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"}\n"
"\n"
"*:hover {\n"
"    background-color: gray;\n"
"    color: white;\n"
"}")
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout.addWidget(self.apply_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.preview_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_label.sizePolicy().hasHeightForWidth())
        self.preview_label.setSizePolicy(sizePolicy)
        self.preview_label.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(20)
        self.preview_label.setFont(font)
        self.preview_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.preview_label.setStyleSheet("*{\n"
"    background-color: black;\n"
"    color: white;\n"
"}")
        self.preview_label.setAlignment(QtCore.Qt.AlignCenter)
        self.preview_label.setObjectName("preview_label")
        self.verticalLayout_2.addWidget(self.preview_label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Configurações"))
        self.label.setText(_translate("MainWindow", "Fonte:"))
        self.preview_text_line_edit.setText(_translate("MainWindow", "Texto de teste"))
        self.view_button.setText(_translate("MainWindow", "Visualizar"))
        self.apply_button.setText(_translate("MainWindow", "Aplicar"))
        self.preview_label.setText(_translate("MainWindow", "Texto de teste"))
