from PySide2.QtWidgets import QDialog
from GerarRelatorio import Ui_Dialog

class GerarRelatorioDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)