from PyQt6.QtGui import QFont, QCloseEvent
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout

from App.MainWindow import MainWindow
from App.NewUserDialog import NewUserDialog


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainWindow = None
        self.passwordEdit = None
        self.registrationDialog = None
        self.loginIsSuccessful = False

        self.setFixedSize(360, 220)
        self.setWindowTitle("Login")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        mainLayout = QVBoxLayout(self)

        loginLabel = QLabel("Login")
        loginLabel.setFont(QFont("Arial", 20))
        mainLayout.addWidget(loginLabel)

        usernameLayout = QHBoxLayout()
        mainLayout.addLayout(usernameLayout)

        usernameLabel = QLabel("Username:", self)
        usernameLayout.addWidget(usernameLabel)

        usernameEdit = QLineEdit(self)
        usernameEdit.resize(250, 24)
        usernameLayout.addWidget(usernameEdit)

        passwordLayout = QHBoxLayout()
        mainLayout.addLayout(passwordLayout)

        passwordLabel = QLabel("Password:", self)
        passwordLayout.addWidget(passwordLabel)

        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEdit.resize(250, 24)
        passwordLayout.addWidget(self.passwordEdit)

        showPasswordCheckbox = QCheckBox("Show Password", self)
        showPasswordCheckbox.toggled.connect(self.onClickShowPasswordIfChecked)
        mainLayout.addWidget(showPasswordCheckbox)

        loginButton = QPushButton("Login", self)
        loginButton.resize(320, 24)
        loginButton.clicked.connect(self.onClickLoginButton)
        mainLayout.addWidget(loginButton)

        notMemberLabel = QLabel("Not a member?", self)
        mainLayout.addWidget(notMemberLabel)

        signUpButton = QPushButton("Sign Up", self)
        signUpButton.clicked.connect(self.onClickCreateNewUser)
        mainLayout.addWidget(signUpButton)

    def onClickShowPasswordIfChecked(self, checked):
        if checked:
            self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif not checked:
            self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

    def onClickLoginButton(self):
        self.loginIsSuccessful = True
        self.close()
        self.openApplicationWindow()

    def onClickCreateNewUser(self):
        self.registrationDialog = NewUserDialog()
        self.registrationDialog.show()

    def openApplicationWindow(self):
        self.mainWindow = MainWindow()
        self.mainWindow.show()

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.loginIsSuccessful:
            event.accept()
        else:
            answer = QMessageBox.question(
                self, "Quit Application?",
                "Are you sure you want to QUIT?",
                QMessageBox.StandardButton.No | \
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.Yes)
            if answer == QMessageBox.StandardButton.Yes:
                event.accept()
            if answer == QMessageBox.StandardButton.No:
                event.ignore()
