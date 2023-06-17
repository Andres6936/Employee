from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QFont, QRegularExpressionValidator
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QVBoxLayout, QFormLayout


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

        self.usernameEdit = QLineEdit(self)
        self.usernameEdit.resize(250, 24)

        fullNameEdit = QLineEdit(self)
        fullNameEdit.resize(250, 24)

        self.emailEdit = QLineEdit(self)
        self.emailEdit.setPlaceholderText("<username>@<domain>.com")
        regex = QRegularExpression(
            "\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[com]{3}\\b",
            QRegularExpression.PatternOption.CaseInsensitiveOption)
        self.emailEdit.setValidator(QRegularExpressionValidator(regex))

        self.newPasswordEdit = QLineEdit(self)
        self.newPasswordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.newPasswordEdit.resize(250, 24)

        self.confirmEdit = QLineEdit(self)
        self.confirmEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirmEdit.resize(250, 24)

        self.feedbackLabel = QLabel()
        self.feedbackLabel.setAlignment(Qt.AlignmentFlag.AlignBottom)

        signUpButton = QPushButton("Sign Up", self)
        signUpButton.resize(320, 32)
        signUpButton.clicked.connect(self.onClickSignUp)

        mainForm = QFormLayout()
        mainForm.setFieldGrowthPolicy(mainForm.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        mainForm.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        mainForm.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        mainForm.addRow("Username", self.usernameEdit)
        mainForm.addRow("Fullname", fullNameEdit)
        mainForm.addRow("Email", self.emailEdit)
        mainForm.addRow("Password", self.newPasswordEdit)
        mainForm.addRow("Confirm", self.confirmEdit)

        root.addLayout(mainForm)
        root.addWidget(self.feedbackLabel)
        root.addWidget(signUpButton)

        self.setLayout(root)

    def onClickSignUp(self):
        usernameText = self.usernameEdit.text()
        passwordText = self.newPasswordEdit.text()
        confirmText = self.confirmEdit.text()

        self.feedbackLabel.clear()

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

        elif not self.emailEdit.hasAcceptableInput():
            self.feedbackLabel.setText("The email entered incorrectly.")
