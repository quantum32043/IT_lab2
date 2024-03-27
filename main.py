import sys
import re

from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

from ui import Ui_MainWindow
from LFSR import LFSR
from tools import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        regex = QRegularExpression("^[01]{0,25}$")
        validator = QRegularExpressionValidator(regex, self)
        self.ui.StartConditionEdit.setValidator(validator)
        lfsr = LFSR([2, 24])
        self.ui.StartConditionEdit.textEdited.connect(self.register_on_change)
        self.ui.PlainTextEdit.textChanged.connect(self.register_on_change)
        self.ui.OpenFileButton.clicked.connect(self.open_file)
        self.ui.SaveFileButton.clicked.connect(self.save_file)
        self.ui.EncryptButton.clicked.connect(self.take_key(lfsr))

        # self.ui.KeyEdit.setPlainText(lisxt_to_string(lfsr.generate_key(self.ui.StartConditionEdit.toPlainText(), len(data))))

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open", "", "")
        if file_name:
            self.ui.PlainTextEdit.setPlainText(list_to_string((file_to_binary(file_name))))

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save", "", "")
        if file_name:
            with open(file_name, 'wb') as file:
                file.write(bits_to_bytes(self.ui.PlainTextEdit.toPlainText()))

    def register_on_change(self):
        if len(self.ui.StartConditionEdit.text()) == 25 and len(self.ui.PlainTextEdit.toPlainText()) > 0:
            self.ui.EncryptButton.setEnabled(True)
        else:
            self.ui.EncryptButton.setEnabled(False)

    def take_key(self, lfsr):
        self.ui.KeyEdit.setPlainText(list_to_string(lfsr.generate_key(self.ui.StartConditionEdit.text())))


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
