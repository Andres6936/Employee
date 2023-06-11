import sys

from PyQt6.QtWidgets import QApplication, QWidget


class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Empty Window in Qt")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())
