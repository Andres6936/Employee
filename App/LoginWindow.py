from PyQt6.QtGui import QFont, QCloseEvent
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout

from App.MainWindow import MainWindow
from App.NewUserDialog import NewUserDialog


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainWindow = None
        self.loginButton = None
        self.passwordEdit = None
        self.registrationDialog = None
        self.loginIsSuccessful = False

        self.usernameText = ""
        self.passwordText = ""

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
        usernameEdit.textChanged.connect(self.onTextChangedUsername)
        usernameLayout.addWidget(usernameEdit)

        passwordLayout = QHBoxLayout()
        mainLayout.addLayout(passwordLayout)

        passwordLabel = QLabel("Password:", self)
        passwordLayout.addWidget(passwordLabel)

        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEdit.resize(250, 24)
        self.passwordEdit.textChanged.connect(self.onTextChangedPassword)
        passwordLayout.addWidget(self.passwordEdit)

        showPasswordCheckbox = QCheckBox("Show Password", self)
        showPasswordCheckbox.toggled.connect(self.onClickShowPasswordIfChecked)
        mainLayout.addWidget(showPasswordCheckbox)

        self.loginButton = QPushButton("Login", self)
        self.loginButton.resize(320, 24)
        self.loginButton.setEnabled(False)
        self.loginButton.clicked.connect(self.onClickLoginButton)
        mainLayout.addWidget(self.loginButton)

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

    def validateUsernameAndPassword(self):
        if len(self.usernameText) == 0 or len(self.passwordText) == 0:
            self.loginButton.setEnabled(False)
        else:
            self.loginButton.setEnabled(True)

    def onTextChangedUsername(self, username: str):
        self.usernameText = username
        self.validateUsernameAndPassword()

    def onTextChangedPassword(self, password: str):
        self.passwordText = password
        self.validateUsernameAndPassword()

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
