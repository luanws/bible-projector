import sys

import sqlalchemy.ext.baked
import sqlalchemy.sql.default_comparator
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from src.ui.main import MainWindow
from src.utils import styles


def main():
    app = QApplication(sys.argv)

    splash_screen = QSplashScreen(QPixmap('data/img/splash.png'))
    splash_screen.show()

    main_window = MainWindow()
    main_window.showMaximized()

    splash_screen.close()

    app.setStyleSheet(styles.get_qss_stylesheet('src/styles/global.qss'))
    app.exec()


if __name__ == '__main__':
    main()
