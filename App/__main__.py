import sys

from PyQt6.QtWidgets import QApplication
from dotenv import load_dotenv

from App.SceneManager import SceneManager

if __name__ == '__main__':
    # Take environment variables from .env
    load_dotenv()

    app = QApplication(sys.argv)
    window = SceneManager()
    sys.exit(app.exec())
