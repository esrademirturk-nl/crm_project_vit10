import os
import subprocess
import sys
import time
import requests

from PyQt5.QtWidgets import QApplication
from ui.screens.applications_window import ApplicationsWindow


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
API_BASE = "http://127.0.0.1:8000"


def start_backend():
    env = os.environ.copy()

    env["PYTHONPATH"] = PROJECT_ROOT + os.pathsep + env.get("PYTHONPATH", "")

    return subprocess.Popen(
        [
            sys.executable, "-m", "uvicorn",
            "backend.main:app",
            "--host", "127.0.0.1",
            "--port", "8000",
        ],
        cwd=PROJECT_ROOT,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )


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
    backend = start_backend()

    try:
        if not wait_backend():
            #backend loglari gosterme
            if backend.stdout:
                logs = backend.stdout.read()[-4000:] 
            else:
                logs = "No logs captured."
            raise RuntimeError("Backend did not start in time.\n\nLast logs:\n" + logs)

        app = QApplication(sys.argv)
        window = ApplicationsWindow()
        window.show()
        code = app.exec_()
        

    finally:
        # backend'i kapat
        backend.terminate()
        try:
            backend.wait(timeout=5)
        except subprocess.TimeoutExpired:
            backend.kill()

    sys.exit(code)
