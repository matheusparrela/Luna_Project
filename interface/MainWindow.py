# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledALhvhD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import curvaDeEmpuxo.CurvaEmpuxo as ce
import numpy

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(884, 696)

        self.actionCr_ditos = QAction(MainWindow)
        self.actionCr_ditos.setObjectName(u"actionCr_ditos")
        self.actionCdigo_Fonte = QAction(MainWindow)
        self.actionCdigo_Fonte.setObjectName(u"actionCdigo_Fonte")
        self.actionReportar_Erro = QAction(MainWindow)
        self.actionReportar_Erro.setObjectName(u"actionReportar_Erro")
        self.actionComo_Usar = QAction(MainWindow)
        self.actionComo_Usar.setObjectName(u"actionComo_Usar")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 190, 861, 461))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 10, 831, 411))

        self.tab = QWidget()
        self.tab.setObjectName(u"tab")

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 0, 601, 381))

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")

        self.tableWidget = QTableWidget(self.tab_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 811, 421))
        self.tabWidget.addTab(self.tab_2, "")

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(730, 430, 121, 21))

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 70, 861, 121))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(750, 90, 101, 25))
        self.pushButton_2.clicked.connect(self.gerarGrafico)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 171, 21))

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(600, 50, 251, 25))

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(180, 50, 271, 25))

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 50, 141, 21))

        # Explorador de Arquivos
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 101, 21))

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 20, 651, 25))

        self.layout = QVBoxLayout()
        self.pushButton = QPushButton("Selecionar Arquivo", self.frame_2)
        self.pushButton.clicked.connect(self.show_file_dialog)
        self.layout.addWidget(self.pushButton)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(760, 20, 89, 25))

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(360, 0, 141, 21))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 884, 22))
        self.menuAjuda = QMenu(self.menuBar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        self.menuSobre = QMenu(self.menuBar)
        self.menuSobre.setObjectName(u"menuSobre")
        self.menuSair = QMenu(self.menuBar)
        self.menuSair.setObjectName(u"menuSair")
        self.menuFerramentas = QMenu(self.menuBar)
        self.menuFerramentas.setObjectName(u"menuFerramentas")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFerramentas.menuAction())
        self.menuBar.addAction(self.menuAjuda.menuAction())
        self.menuBar.addAction(self.menuSobre.menuAction())
        self.menuBar.addAction(self.menuSair.menuAction())
        self.menuAjuda.addAction(self.actionComo_Usar)
        self.menuAjuda.addSeparator()
        self.menuAjuda.addAction(self.actionReportar_Erro)
        self.menuSobre.addAction(self.actionCr_ditos)
        self.menuSobre.addAction(self.actionCdigo_Fonte)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    def show_file_dialog(self):

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)

        if file_dialog.exec_() == QFileDialog.Accepted:
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                self.lineEdit.setText(file_paths[0])


    def gerarGrafico(self):

        file = str(self.lineEdit.text())  # Arquivo de dados
        min = float(self.lineEdit_3.text())  # Empuxo mínimo para definir o início e fim da curva (N)
        massa = float(self.lineEdit_2.text())  # Massa de propelente (kg)
        Empuxo = ce.CurvaEmpuxo(file, min, massa)
        Empuxo.all()
        self.img()
        self.populate_table(Empuxo.table)

    def img(self):
        pixmap = QPixmap("../curvaDeEmpuxo/img/grafico.png")
        # Redimensionar a imagem para o tamanho desejado
        pixmap = pixmap.scaled(600, 400)
        # Exibir a imagem no QLabel
        self.label_4.setPixmap(pixmap)

    def populate_table(self, table):

        self.tableWidget.setColumnCount(len(table[0]))
        self.tableWidget.setRowCount(len(table))

        self.layout = QVBoxLayout(self.tableWidget)  # Layout vertical para centralizar a tabela
        self.layout.setAlignment(Qt.AlignCenter)

        headers = ["Propriedade", "Valor", "Unidade"]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem(str(table[row][col]))
                self.tableWidget.setItem(row, col, item)

        self.tableWidget.resizeColumnsToContents()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Curva de Empuxo", None))
        self.actionCr_ditos.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9ditos", None))
        self.actionCdigo_Fonte.setText(QCoreApplication.translate("MainWindow", u"Codigo Fonte", None))
        self.actionReportar_Erro.setText(QCoreApplication.translate("MainWindow", u"Reportar Erro", None))
        self.actionComo_Usar.setText(QCoreApplication.translate("MainWindow", u"Como Usar", None))
        self.label_4.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("MainWindow", u"Gr\u00e1fico", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("MainWindow", u"Dados", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Gerar  Relat\u00f3rio", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Peso do Propelente (Kg):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Empuxo M\u00ednimo (N):", None))
        self.lineEdit.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Abrir arquivo:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CURVA DE EMPUXO", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.menuSobre.setTitle(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.menuSair.setTitle(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.menuFerramentas.setTitle(QCoreApplication.translate("MainWindow", u"Ferramentas", None))
    # retranslateUi


