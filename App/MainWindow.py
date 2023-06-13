from PyQt6.QtWidgets import QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(640, 426)
        self.setWindowTitle("Main Window")
