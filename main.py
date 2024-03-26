import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from ui import Ui_MainWindow
from LFSR import LFSR
from tools import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        lfsr = LFSR([0, 3])
        #print(lfsr.file_to_binary("D:/1.txt"))
        data = file_to_binary("D:/1.txt")
        self.ui.StartConditionEdit.setPlainText("1111")
        self.ui.KeyEdit.setPlainText(lisxt_to_string(lfsr.generate_key(self.ui.StartConditionEdit.toPlainText(), len(data))))


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())