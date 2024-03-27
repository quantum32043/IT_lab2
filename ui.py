# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerwxswaL.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QPlainTextEdit, QPushButton, QWidget, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.StartConditionLabel = QLabel(self.centralwidget)
        self.StartConditionLabel.setObjectName(u"StartConditionLabel")
        self.StartConditionLabel.setGeometry(QRect(30, 25, 350, 25))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.StartConditionLabel.setFont(font)
        self.StartConditionEdit = QLineEdit(self.centralwidget)
        self.StartConditionEdit.setObjectName(u"StartConditionEdit")
        self.StartConditionEdit.setGeometry(QRect(30, 55, 300, 30))
        font1 = QFont()
        font1.setPointSize(14)
        self.StartConditionEdit.setFont(font1)
        self.KeyEdit = QPlainTextEdit(self.centralwidget)
        self.KeyEdit.setObjectName(u"KeyEdit")
        self.KeyEdit.setGeometry(QRect(30, 120, 300, 75))
        self.KeyEdit.setFont(font1)
        self.KeyEdit.setReadOnly(True)
        self.KeyLabel = QLabel(self.centralwidget)
        self.KeyLabel.setObjectName(u"KeyLabel")
        self.KeyLabel.setGeometry(QRect(30, 90, 300, 25))
        self.KeyLabel.setFont(font1)
        self.PlainTextEdit = QPlainTextEdit(self.centralwidget)
        self.PlainTextEdit.setObjectName(u"PlainTextEdit")
        self.PlainTextEdit.setGeometry(QRect(30, 250, 255, 100))
        self.PlainTextEdit.setFont(font1)
        self.CipherTextEdit = QPlainTextEdit(self.centralwidget)
        self.CipherTextEdit.setObjectName(u"CipherEditLabel")
        self.CipherTextEdit.setGeometry(QRect(315, 250, 255, 100))
        self.CipherTextEdit.setFont(font1)
        self.PlainFileLabel = QLabel(self.centralwidget)
        self.PlainFileLabel.setObjectName(u"PlainFileLabel")
        self.PlainFileLabel.setGeometry(QRect(30, 220, 251, 25))
        self.PlainFileLabel.setFont(font1)
        self.PlainFileLabel.setText("Бинарный код файла:")
        self.CipherFileLabel = QLabel(self.centralwidget)
        self.CipherFileLabel.setObjectName(u"CipherFileLabel")
        self.CipherFileLabel.setGeometry(QRect(315, 220, 251, 25))
        self.CipherFileLabel.setFont(font1)
        self.CipherFileLabel.setFont(font1)
        self.CipherFileLabel.setText("Результат:")
        self.EncryptButton = QPushButton(self.centralwidget)
        self.EncryptButton.setObjectName(u"EncryptButton")
        self.EncryptButton.setEnabled(False)
        self.EncryptButton.setGeometry(QRect(370, 50, 200, 30))
        self.EncryptButton.setFont(font1)
        self.DecryptButton = QPushButton(self.centralwidget)
        self.DecryptButton.setObjectName(u"DecryptButton")
        self.DecryptButton.setEnabled(False)
        self.DecryptButton.setGeometry(QRect(370, 90, 200, 30))
        self.DecryptButton.setFont(font1)
        self.OpenFileButton = QPushButton(self.centralwidget)
        self.OpenFileButton.setObjectName(u"OpenFileButton")
        self.OpenFileButton.setEnabled(True)
        self.OpenFileButton.setGeometry(QRect(370, 130, 110, 25))
        self.OpenFileButton.setText("Открыть файл...")
        self.SaveFileButton = QPushButton(self.centralwidget)
        self.SaveFileButton.setObjectName(u"SaveFileButton")
        self.SaveFileButton.setEnabled(True)
        self.SaveFileButton.setGeometry(QRect(370, 165, 110, 25))
        self.SaveFileButton.setText("Сохранить файл...")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.StartConditionLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430:", None))
        self.KeyLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u043a\u043b\u044e\u0447:", None))
        self.EncryptButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.DecryptButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

