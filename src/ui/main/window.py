# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\GitHub\bible-projector\python\src\ui\main\window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


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
        self.versoesComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.versoesComboBox.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 4px;\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"    width: 30px\n"
"}")
        self.versoesComboBox.setObjectName("versoesComboBox")
        self.horizontalLayout_3.addWidget(self.versoesComboBox)
        self.pesquisaLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pesquisaLineEdit.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.pesquisaLineEdit.setObjectName("pesquisaLineEdit")
        self.horizontalLayout_3.addWidget(self.pesquisaLineEdit)
        self.pesquisarButton = QtWidgets.QPushButton(self.centralwidget)
        self.pesquisarButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pesquisarButton.setStyleSheet("* {\n"
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
        self.pesquisarButton.setObjectName("pesquisarButton")
        self.horizontalLayout_3.addWidget(self.pesquisarButton)
        self.projetarButton = QtWidgets.QPushButton(self.centralwidget)
        self.projetarButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.projetarButton.setStyleSheet("* {\n"
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
        self.projetarButton.setObjectName("projetarButton")
        self.horizontalLayout_3.addWidget(self.projetarButton)
        self.atualizarButton = QtWidgets.QPushButton(self.centralwidget)
        self.atualizarButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.atualizarButton.setStyleSheet("* {\n"
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
        self.atualizarButton.setObjectName("atualizarButton")
        self.horizontalLayout_3.addWidget(self.atualizarButton)
        self.configuracoesButton = QtWidgets.QPushButton(self.centralwidget)
        self.configuracoesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configuracoesButton.setStyleSheet("* {\n"
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
        self.configuracoesButton.setObjectName("configuracoesButton")
        self.horizontalLayout_3.addWidget(self.configuracoesButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.chapterListView = QtWidgets.QListView(self.centralwidget)
        self.chapterListView.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}")
        self.chapterListView.setObjectName("chapterListView")
        self.gridLayout.addWidget(self.chapterListView, 3, 0, 1, 1)
        self.occurrencesListView = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.occurrencesListView.sizePolicy().hasHeightForWidth())
        self.occurrencesListView.setSizePolicy(sizePolicy)
        self.occurrencesListView.setMaximumSize(QtCore.QSize(500, 16777215))
        self.occurrencesListView.setStyleSheet("* {\n"
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
        self.occurrencesListView.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.occurrencesListView.setWordWrap(True)
        self.occurrencesListView.setObjectName("occurrencesListView")
        self.gridLayout.addWidget(self.occurrencesListView, 1, 3, 3, 1)
        self.ocorrenciasLabel = QtWidgets.QLabel(self.centralwidget)
        self.ocorrenciasLabel.setStyleSheet("")
        self.ocorrenciasLabel.setObjectName("ocorrenciasLabel")
        self.gridLayout.addWidget(self.ocorrenciasLabel, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.previewTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewTextEdit.sizePolicy().hasHeightForWidth())
        self.previewTextEdit.setSizePolicy(sizePolicy)
        self.previewTextEdit.setMaximumSize(QtCore.QSize(16777215, 200))
        self.previewTextEdit.setStyleSheet("* {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}")
        self.previewTextEdit.setObjectName("previewTextEdit")
        self.gridLayout.addWidget(self.previewTextEdit, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
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
        self.pesquisarButton.setText(_translate("MainWindow", "Pesquisar"))
        self.projetarButton.setText(_translate("MainWindow", "Projetar"))
        self.atualizarButton.setText(_translate("MainWindow", "Atualizar"))
        self.configuracoesButton.setText(_translate("MainWindow", "Configurações"))
        self.ocorrenciasLabel.setText(_translate("MainWindow", "Ocorrências"))
        self.label_3.setText(_translate("MainWindow", "Capítulo"))
        self.label_2.setText(_translate("MainWindow", "Pré-visualização"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
