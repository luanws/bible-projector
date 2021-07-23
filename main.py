import sys

import sqlalchemy.ext.baked
import sqlalchemy.sql.default_comparator
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

from src.ui.main import MainWindow

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowIcon(QtGui.QIcon('icon.ico'))
    main_window.showMaximized()
    app.exec()

if __name__ == '__main__':
    main()
