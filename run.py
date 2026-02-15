import sys
import time
import requests
from threading import Thread

import uvicorn
from PyQt5.QtWidgets import QApplication
from ui.screens.login_window import LoginWindow
import sys
from multiprocessing import freeze_support

def _fix_frozen_paths():
    # PyInstaller içinde çalışıyorsak
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base = sys._MEIPASS
        # bundle içindeki kökü sys.path'e ekle (backend/ui importları için)
        if base not in sys.path:
            sys.path.insert(0, base)

_fix_frozen_paths()
freeze_support()

API_BASE = "http://127.0.0.1:8000"

def start_backend_inprocess():
    config = uvicorn.Config(
        "backend.main:app",
        host="127.0.0.1",
        port=8000,
        log_level="warning",
    )
    server = uvicorn.Server(config)

    t = Thread(target=server.run, daemon=True)
    t.start()
    return server, t

def wait_backend(timeout_sec=15):
    start = time.time()
    while time.time() - start < timeout_sec:
        try:
            r = requests.get(f"{API_BASE}/docs", timeout=2)
            if r.status_code == 200:
                return True
        except Exception:
            time.sleep(0.3)
    return False

if __name__ == "__main__":
    server, t = start_backend_inprocess()

    try:
        if not wait_backend():
            raise RuntimeError("Backend did not start in time.")

        app = QApplication(sys.argv)
        window = LoginWindow()
        window.show()
        code = app.exec_()
    finally:
        # uvicorn'u kapat
        server.should_exit = True

    sys.exit(code)
