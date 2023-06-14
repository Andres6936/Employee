import sys

from dotenv import load_dotenv
from PyQt6.QtWidgets import QApplication

from App.LoginWindow import LoginWindow

if __name__ == '__main__':
    # Take environment variables from .env
    load_dotenv()

    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
