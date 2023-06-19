from PyQt6.QtWidgets import QWidget, QStackedLayout

from App.LoginWindow import LoginWindow
from App.MainWindow import MainWindow
from App.NewUserWindow import NewUserWindow
from App.Scene.ISceneManager import ISceneManager


class SceneManager(QWidget):
    __metaclass__ = ISceneManager

    def __init__(self):
        super().__init__()
        self.setFixedSize(375, 667)
        self.setObjectName("SceneManager")
        self.setStyleSheet("""
            QWidget#SceneManager {
                background-color: white
            }
        """)

        self.loginWindow = LoginWindow(self)
        self.newUserWindow = NewUserWindow()
        self.mainWindow = MainWindow()

        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.loginWindow)
        self.stackedLayout.addWidget(self.newUserWindow)
        self.stackedLayout.addWidget(self.mainWindow)

        self.setLayout(self.stackedLayout)
        self.show()

    def nextScene(self, scene):
        self.stackedLayout.setCurrentIndex(scene)
