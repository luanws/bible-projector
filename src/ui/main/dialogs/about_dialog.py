from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout
from src.version import version


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)

        self.setWindowTitle("Sobre")
        self.setWindowIcon(QIcon('icon.ico'))
        self.setFixedSize(400, 200)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

        self.title_label = QLabel("Projetor bíblico")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
        """)
        self.title_label.setFixedSize(400, 50)
        self.layout.addWidget(self.title_label)

        self.version_label = QLabel(f"Versão: {version}")
        self.version_label.setAlignment(Qt.AlignCenter)
        self.version_label.setStyleSheet("font-size: 12px;")
        self.version_label.setFixedSize(400, 50)
        self.layout.addWidget(self.version_label)

        text = "Este é um aplicativo para projetar versículos da Bíblia."
        self.text_label = QLabel(text)
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet("font-size: 12px;")
        self.text_label.setFixedSize(400, 50)
        self.layout.addWidget(self.text_label)

        self.setWindowFlags(self.windowFlags() & ~
                            Qt.WindowContextHelpButtonHint)
