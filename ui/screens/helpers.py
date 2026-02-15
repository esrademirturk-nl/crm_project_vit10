from PyQt5 import QtWidgets, QtGui,QtCore
import os
import sys

def resource_path(rel_path: str) -> str:
    # PyInstaller bundle içindeyken dosyalar sys._MEIPASS altında olur
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, rel_path)

def make_flat_icon(color_hex: str, symbol: str):
    size = 48
    pm = QtGui.QPixmap(size, size)
    pm.fill(QtCore.Qt.white)  # ikon arka planı beyaz

    painter = QtGui.QPainter(pm)
    painter.setRenderHint(QtGui.QPainter.Antialiasing)

    font = QtGui.QFont("Arial", 28, QtGui.QFont.Bold)
    painter.setFont(font)
    painter.setPen(QtGui.QColor(color_hex))
    painter.drawText(pm.rect(), QtCore.Qt.AlignCenter, symbol)

    painter.end()
    return pm

def show_message(parent, title: str, text: str, kind: str = "info"):

    box = QtWidgets.QMessageBox(parent)
    box.setWindowTitle(title)
    box.setText(text)

    # Beyaz, sade stil
    box.setStyleSheet("""
        QMessageBox {
            background-color: white;
        }
        QLabel {
            background-color: white;
            color: #1f2937;
            font-size: 14px;
        }
        QPushButton {
            background-color: #111827;
            color: white;
            border-radius: 10px;
            padding: 6px 18px;
            min-width: 90px;
        }
        QPushButton:hover {
            background-color: #000000;
        }
    """)

    # Renkli ama flat ikon
    if kind == "success":
        box.setIconPixmap(make_flat_icon("#16a34a", "✓"))
    elif kind == "error":
        box.setIconPixmap(make_flat_icon("#dc2626", "✕"))
    else:
        box.setIconPixmap(make_flat_icon("#2563eb", "i"))

    box.exec_()
   