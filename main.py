import sys

import sqlalchemy.ext.baked
import sqlalchemy.sql.default_comparator
from PyQt5.QtWidgets import QApplication

from src.ui.main import MainWindow
from src.utils import styles


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showMaximized()
    app.setStyleSheet(styles.get_qss_stylesheet('global'))
    app.exec()


if __name__ == '__main__':
    main()
