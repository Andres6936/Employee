from PyQt6.QtWidgets import QWidget, QStackedLayout

from App.LoginWindow import LoginWindow
from App.NewUserWindow import NewUserWindow


class SceneManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(375, 667)

        self.loginWindow = LoginWindow()
        self.newUserWindow = NewUserWindow()

        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.loginWindow)
        self.stackedLayout.addWidget(self.newUserWindow)

        self.setLayout(self.stackedLayout)
        self.show()
