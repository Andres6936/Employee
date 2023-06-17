from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QFont, QRegularExpressionValidator
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QVBoxLayout, QHBoxLayout


class NewUserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(375, 667)
        self.setWindowTitle("Registration")
        root = QVBoxLayout()

        loginLabel = QLabel("Create New Account", self)
        loginLabel.setFont(QFont("Arial", 20))
        loginLabel.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        root.addWidget(loginLabel)

        usernameLayout = QHBoxLayout()
        usernameLabel = QLabel("Username:", self)
        usernameLayout.addWidget(usernameLabel)

        self.usernameEdit = QLineEdit(self)
        self.usernameEdit.resize(250, 24)
        usernameLayout.addWidget(self.usernameEdit)

        root.addLayout(usernameLayout)

        fullNameLayout = QHBoxLayout()
        fullNameLabel = QLabel("Full Name:", self)
        fullNameLayout.addWidget(fullNameLabel)

        fullNameEdit = QLineEdit(self)
        fullNameEdit.resize(250, 24)
        fullNameLayout.addWidget(fullNameEdit)

        root.addLayout(fullNameLayout)

        emailLayout = QHBoxLayout()
        emailLabel = QLabel("Email:", self)
        emailLayout.addWidget(emailLabel)

        emailEdit = QLineEdit(self)
        emailEdit.setPlaceholderText("<username>@<domain>.com")
        regex = QRegularExpression(
            "\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[com]{3}\\b",
            QRegularExpression.PatternOption.CaseInsensitiveOption)
        emailEdit.setValidator(QRegularExpressionValidator(regex))
        emailLayout.addWidget(emailEdit)

        root.addLayout(emailLayout)

        newPasswordLayout = QHBoxLayout()
        newPasswordLabel = QLabel("Password:", self)
        newPasswordLayout.addWidget(newPasswordLabel)

        self.newPasswordEdit = QLineEdit(self)
        self.newPasswordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.newPasswordEdit.resize(250, 24)
        newPasswordLayout.addWidget(self.newPasswordEdit)

        root.addLayout(newPasswordLayout)

        confirmPasswordLayout = QHBoxLayout()
        confirmLabel = QLabel("Confirm:", self)
        confirmPasswordLayout.addWidget(confirmLabel)

        self.confirmEdit = QLineEdit(self)
        self.confirmEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirmEdit.resize(250, 24)
        confirmPasswordLayout.addWidget(self.confirmEdit)

        root.addLayout(confirmPasswordLayout)

        signUpButton = QPushButton("Sign Up", self)
        signUpButton.resize(320, 32)
        signUpButton.clicked.connect(self.onClickSignUp)
        root.addWidget(signUpButton)

        self.setLayout(root)

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
