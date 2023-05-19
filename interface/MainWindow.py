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
        MainWindow.resize(900, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 190, 871, 511))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 10, 811, 451))

        self.tab = QWidget()
        self.tab.setObjectName(u"tab")

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 10, 600, 400))

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")

        self.tableWidget = QTableWidget(self.tab_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 811, 421))
        self.tabWidget.addTab(self.tab_2, "")

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(740, 470, 116, 25))

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 20, 871, 161))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(750, 130, 101, 25))
        self.pushButton_2.clicked.connect(self.gerarGrafico)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 141, 16))

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(580, 90, 271, 25))

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 90, 301, 25))

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 90, 121, 20))

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 10, 651, 25))

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(760, 10, 89, 25))

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 21))

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")

        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def gerarGrafico(self):

        file = '../curvaDeEmpuxo/files/teste.txt'  # Arquivo de dados
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Gr\u00e1fico", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Dados", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Gerar  Relat\u00f3rio", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Peso do Propelente:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Empuxo M\u00ednimo:", None))
        self.lineEdit.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Abrir arquivo:", None))
    # retranslateUi


