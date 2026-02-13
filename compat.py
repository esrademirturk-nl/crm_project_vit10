try:
    # Önce PyQt6 dene
    from PyQt6.QtWidgets import QApplication
    from PyQt6.QtWidgets import *
    from PyQt6.QtCore import *
    from PyQt6.QtGui import *
    PYQT_VERSION = 6

    # PyQt6 enum düzeltmeleri
    AlignCenter = Qt.AlignmentFlag.AlignCenter
    AlignLeft = Qt.AlignmentFlag.AlignLeft
    AlignRight = Qt.AlignmentFlag.AlignRight

except ImportError:
    # PyQt6 yoksa PyQt5 kullan
    from PyQt6.QtWidgets import QApplication
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    PYQT_VERSION = 5

    # PyQt5 enumlar
    AlignCenter = Qt.AlignCenter
    AlignLeft = Qt.AlignLeft
    AlignRight = Qt.AlignRight

def run_app(app):
    if PYQT_VERSION == 6:
        app.exec()
    else:
        app.exec_()
