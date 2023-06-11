import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.loginIsSuccessful = False

        self.setFixedSize(360, 220)
        self.setWindowTitle("Login")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        loginLabel = QLabel("Login", self)
        loginLabel.setFont(QFont("Arial", 20))
        loginLabel.move(160, 10)

        usernameLabel = QLabel("Username:", self)
        usernameLabel.move(20, 54)

        usernameEdit = QLineEdit(self)
        usernameEdit.resize(250, 24)
        usernameEdit.move(90, 50)

        passwordLabel = QLabel("Password:", self)
        passwordLabel.move(20, 86)

        passwordEdit = QLineEdit(self)
        passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        passwordEdit.resize(250, 24)
        passwordEdit.move(90, 82)

        showPasswordCheckbox = QCheckBox("Show Password", self)
        showPasswordCheckbox.move(90, 110)

        loginButton = QPushButton("Login", self)
        loginButton.resize(320, 24)
        loginButton.move(20, 140)

        notMemberLabel = QLabel("Not a member?", self)
        notMemberLabel.move(20, 186)

    def onClickLoginButton(self):
        self.loginIsSuccessful = True
        self.close()
        self.openApplicationWindow()

    def openApplicationWindow(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
