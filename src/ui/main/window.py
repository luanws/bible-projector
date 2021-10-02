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
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.history_label = QtWidgets.QLabel(self.centralwidget)
        self.history_label.setStyleSheet("")
        self.history_label.setObjectName("history_label")
        self.gridLayout.addWidget(self.history_label, 0, 3, 1, 1)
        self.chapter_label = QtWidgets.QLabel(self.centralwidget)
        self.chapter_label.setObjectName("chapter_label")
        self.gridLayout.addWidget(self.chapter_label, 2, 0, 1, 1)
        self.preview_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_text_edit.sizePolicy().hasHeightForWidth())
        self.preview_text_edit.setSizePolicy(sizePolicy)
        self.preview_text_edit.setMaximumSize(QtCore.QSize(16777215, 160))
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
        self.chapter_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.chapter_list_widget.setStyleSheet("#chapter_list_widget {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}")
        self.chapter_list_widget.setObjectName("chapter_list_widget")
        self.gridLayout.addWidget(self.chapter_list_widget, 3, 0, 1, 1)
        self.history_list_widget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.history_list_widget.sizePolicy().hasHeightForWidth())
        self.history_list_widget.setSizePolicy(sizePolicy)
        self.history_list_widget.setMaximumSize(QtCore.QSize(240, 16777215))
        self.history_list_widget.setStyleSheet("#history_list_widget {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"    padding: 8px;\n"
"}")
        self.history_list_widget.setObjectName("history_list_widget")
        self.gridLayout.addWidget(self.history_list_widget, 1, 3, 3, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuFerramentas = QtWidgets.QMenu(self.menubar)
        self.menuFerramentas.setObjectName("menuFerramentas")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.actionVerificar_se_h_atualiza_es = QtWidgets.QAction(MainWindow)
        self.actionVerificar_se_h_atualiza_es.setObjectName("actionVerificar_se_h_atualiza_es")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_settings = QtWidgets.QAction(MainWindow)
        self.action_settings.setObjectName("action_settings")
        self.action_export_history = QtWidgets.QAction(MainWindow)
        self.action_export_history.setObjectName("action_export_history")
        self.menuArquivo.addAction(self.action_settings)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.action_quit)
        self.menuFerramentas.addAction(self.action_export_history)
        self.menuAjuda.addAction(self.action_about)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuFerramentas.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projetor bíblico"))
        self.search_line_edit.setPlaceholderText(_translate("MainWindow", "Referência (F4)"))
        self.search_button.setText(_translate("MainWindow", "Pesquisar"))
        self.project_button.setText(_translate("MainWindow", "Projetar"))
        self.update_button.setText(_translate("MainWindow", "Atualizar"))
        self.history_label.setText(_translate("MainWindow", "Histórico"))
        self.chapter_label.setText(_translate("MainWindow", "Capítulo"))
        self.preview_label.setText(_translate("MainWindow", "Pré-visualização"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuFerramentas.setTitle(_translate("MainWindow", "Ferramentas"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.action_about.setText(_translate("MainWindow", "Sobre"))
        self.actionVerificar_se_h_atualiza_es.setText(_translate("MainWindow", "Verificar se há atualizações"))
        self.action_quit.setText(_translate("MainWindow", "Sair"))
        self.action_settings.setText(_translate("MainWindow", "Configurações"))
        self.action_export_history.setText(_translate("MainWindow", "Exportar histórico"))
