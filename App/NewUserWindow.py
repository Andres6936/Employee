from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget


class NewUserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(375, 667)
        self.setWindowTitle("Registration")

        loginLabel = QLabel("Create New Account", self)
        loginLabel.setFont(QFont("Arial", 20))
        loginLabel.move(90, 20)

        usernameLabel = QLabel("Username:", self)
        usernameLabel.move(20, 144)

        self.usernameEdit = QLineEdit(self)
        self.usernameEdit.resize(250, 24)
        self.usernameEdit.move(90, 140)

        fullNameLabel = QLabel("Full Name:", self)
        fullNameLabel.move(20, 174)

        fullNameEdit = QLineEdit(self)
        fullNameEdit.resize(250, 24)
        fullNameEdit.move(90, 170)

        newPasswordLabel = QLabel("Password:", self)
        newPasswordLabel.move(20, 204)

        self.newPasswordEdit = QLineEdit(self)
        self.newPasswordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.newPasswordEdit.resize(250, 24)
        self.newPasswordEdit.move(90, 200)

        confirmLabel = QLabel("Confirm:", self)
        confirmLabel.move(20, 234)

        self.confirmEdit = QLineEdit(self)
        self.confirmEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirmEdit.resize(250, 24)
        self.confirmEdit.move(90, 230)

        signUpButton = QPushButton("Sign Up", self)
        signUpButton.resize(320, 32)
        signUpButton.move(20, 270)
        signUpButton.clicked.connect(self.onClickSignUp)

    def onClickSignUp(self):
        usernameText = self.usernameEdit.text()
        passwordText = self.newPasswordEdit.text()
        confirmText = self.confirmEdit.text()

        if usernameText == "" or passwordText == "":
            QMessageBox.warning(
                self, "Error Message",
                "Please enter username or password values.",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)

        elif passwordText != confirmText:
            QMessageBox.warning(
                self, "Error Message",
                "The password you entered do not match.",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
