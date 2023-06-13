from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton


class NewUserDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.setFixedSize(360, 320)
        self.setWindowTitle("Registration")

        loginLabel = QLabel("Create New Account", self)
        loginLabel.setFont(QFont("Arial", 20))
        loginLabel.move(90, 20)

        nameLabel = QLabel("Username:", self)
        nameLabel.move(20, 144)

        nameEdit = QLineEdit(self)
        nameEdit.resize(250, 24)
        nameEdit.move(90, 140)

        fullNameLabel = QLabel("Full Name:", self)
        fullNameLabel.move(20, 174)

        fullNameEdit = QLineEdit(self)
        fullNameEdit.resize(250, 24)
        fullNameEdit.move(90, 170)

        newPasswordLabel = QLabel("Password:", self)
        newPasswordLabel.move(20, 204)

        newPasswordEdit = QLineEdit(self)
        newPasswordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        newPasswordEdit.resize(250, 24)
        newPasswordEdit.move(90, 200)

        confirmLabel = QLabel("Confirm:", self)
        confirmLabel.move(20, 234)

        confirmEdit = QLineEdit(self)
        confirmEdit.setEchoMode(QLineEdit.EchoMode.Password)
        confirmEdit.resize(250, 24)
        confirmEdit.move(90, 230)

        signUpButton = QPushButton("Sign Up", self)
        signUpButton.resize(320, 32)
        signUpButton.move(20, 270)
        signUpButton.clicked.connect(self.onClickSignUp)

    def onClickSignUp(self):
        pass
