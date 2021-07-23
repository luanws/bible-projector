from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.versions_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.versions_combo_box.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 4px;\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"    width: 30px\n"
"}")
        self.versions_combo_box.setObjectName("versions_combo_box")
        self.horizontalLayout_3.addWidget(self.versions_combo_box)
        self.search_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_line_edit.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.search_line_edit.setObjectName("search_line_edit")
        self.horizontalLayout_3.addWidget(self.search_line_edit)
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_button.setStyleSheet("* {\n"
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
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_3.addWidget(self.search_button)
        self.project_button = QtWidgets.QPushButton(self.centralwidget)
        self.project_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.project_button.setStyleSheet("* {\n"
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
        self.project_button.setObjectName("project_button")
        self.horizontalLayout_3.addWidget(self.project_button)
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.update_button.setStyleSheet("* {\n"
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
        self.update_button.setObjectName("update_button")
        self.horizontalLayout_3.addWidget(self.update_button)
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_button.setStyleSheet("* {\n"
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
        self.settings_button.setObjectName("settings_button")
        self.horizontalLayout_3.addWidget(self.settings_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.chapter_list_view = QtWidgets.QListView(self.centralwidget)
        self.chapter_list_view.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}")
        self.chapter_list_view.setObjectName("chapter_list_view")
        self.gridLayout.addWidget(self.chapter_list_view, 3, 0, 1, 1)
        self.occurrences_list_view = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.occurrences_list_view.sizePolicy().hasHeightForWidth())
        self.occurrences_list_view.setSizePolicy(sizePolicy)
        self.occurrences_list_view.setMaximumSize(QtCore.QSize(500, 16777215))
        self.occurrences_list_view.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"*:item {\n"
"    margin-bottom: 10px;\n"
"}")
        self.occurrences_list_view.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.occurrences_list_view.setWordWrap(True)
        self.occurrences_list_view.setObjectName("occurrences_list_view")
        self.gridLayout.addWidget(self.occurrences_list_view, 1, 3, 3, 1)
        self.occurrences_label = QtWidgets.QLabel(self.centralwidget)
        self.occurrences_label.setStyleSheet("")
        self.occurrences_label.setObjectName("occurrences_label")
        self.gridLayout.addWidget(self.occurrences_label, 0, 3, 1, 1)
        self.chapter_label = QtWidgets.QLabel(self.centralwidget)
        self.chapter_label.setObjectName("chapter_label")
        self.gridLayout.addWidget(self.chapter_label, 2, 0, 1, 1)
        self.preview_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_text_edit.sizePolicy().hasHeightForWidth())
        self.preview_text_edit.setSizePolicy(sizePolicy)
        self.preview_text_edit.setMaximumSize(QtCore.QSize(16777215, 200))
        self.preview_text_edit.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}")
        self.preview_text_edit.setObjectName("preview_text_edit")
        self.gridLayout.addWidget(self.preview_text_edit, 1, 0, 1, 1)
        self.preview_label = QtWidgets.QLabel(self.centralwidget)
        self.preview_label.setObjectName("preview_label")
        self.gridLayout.addWidget(self.preview_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projetor bíblico"))
        self.search_button.setText(_translate("MainWindow", "Pesquisar"))
        self.project_button.setText(_translate("MainWindow", "Projetar"))
        self.update_button.setText(_translate("MainWindow", "Atualizar"))
        self.settings_button.setText(_translate("MainWindow", "Configurações"))
        self.occurrences_label.setText(_translate("MainWindow", "Ocorrências"))
        self.chapter_label.setText(_translate("MainWindow", "Capítulo"))
        self.preview_label.setText(_translate("MainWindow", "Pré-visualização"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
