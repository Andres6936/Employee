from PyQt6.QtWidgets import QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(375, 667)
        self.setWindowTitle("Main Window")
