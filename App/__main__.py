import sys

from PyQt6.QtWidgets import QApplication

from App.LoginWindow import LoginWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
