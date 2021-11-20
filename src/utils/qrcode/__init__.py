from PyQt5.QtGui import QPixmap

import qrcode

from .base_image import Image


def make_pixmap(text: str) -> QPixmap:
    qr: Image = qrcode.make(text, image_factory=Image)
    return qr.pixmap()
