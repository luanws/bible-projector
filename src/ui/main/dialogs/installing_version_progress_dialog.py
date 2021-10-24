from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QProgressDialog


class InstallingVersionProgressDialog(QProgressDialog):
    def __init__(self, parent=None):
        super(InstallingVersionProgressDialog, self).__init__(parent)

        self.setWindowIcon(QIcon('icon.ico'))
        self.setWindowTitle('Instalando versão')
        self.setMaximum(100)
        self.setCancelButton(None)
        self.setWindowFlags(self.windowFlags() & ~
                            Qt.WindowContextHelpButtonHint)
