from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCloseEvent, QIcon, QAction
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, \
    QFormLayout, QHBoxLayout

from App.MainWindow import MainWindow
from App.Scene.ISceneManager import ISceneManager


class LoginWindow(QWidget):
    def __init__(self, parent: ISceneManager):
        super().__init__()
        self.parent: ISceneManager = parent

        self.mainWindow = None
        self.loginButton = None
        self.passwordEdit = None
        self.registrationDialog = None
        self.loginIsSuccessful = False
        self.registerNewUser = False

        self.usernameText = ""
        self.passwordText = ""

        self.setFixedSize(375, 667)
        self.setWindowTitle("Login")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        mainLayout = QVBoxLayout(self)

        illustrationLayout = QHBoxLayout()
        illustration = QSvgWidget('./Illustrations/Enter-Password-1.svg')
        illustrationLayout.addWidget(illustration, alignment=Qt.AlignmentFlag.AlignCenter)

        mainLayout.addLayout(illustrationLayout)

        loginLabel = QLabel("Login")
        loginLabel.setObjectName("LoginTitle")

        emailEdit = QLineEdit(self)
        emailEdit.setPlaceholderText("Email ID")
        emailEdit.textChanged.connect(self.onTextChangedUsername)

        actionShowPassword = QAction(self)
        actionShowPassword.setIcon(QIcon('./Icons/Eye-Slash-Fill.svg'))
        actionShowPassword.triggered.connect(self.onClickShowPasswordIfChecked)

        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setPlaceholderText("Password")
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEdit.addAction(actionShowPassword, QLineEdit.ActionPosition.TrailingPosition)
        self.passwordEdit.textChanged.connect(self.onTextChangedPassword)

        forgotPasswordLabel = QPushButton("Forgot Password?")
        forgotPasswordLabel.setObjectName("LinkButton")
        forgotPasswordLabel.setFlat(True)
        forgotPasswordLabel.clicked.connect(self.onClickForgotPassword)

        self.loginButton = QPushButton("Login", self)
        self.loginButton.setObjectName("LoginButton")
        self.loginButton.clicked.connect(self.onClickLoginButton)

        labelOR = QLabel("OR")
        labelOR.setAlignment(Qt.AlignmentFlag.AlignCenter)
        labelOR.setStyleSheet("""
            color: #878787;
            font: normal 13px 'Monospace';
        """)

        loginGoogleButton = QPushButton("Login with Google")
        loginGoogleButton.setObjectName("LoginGoogleButton")

        mainForm = QFormLayout()
        mainForm.setFieldGrowthPolicy(mainForm.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        mainForm.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainForm.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        mainForm.addRow(loginLabel)
        mainForm.addRow(emailEdit)
        mainForm.addRow(self.passwordEdit)
        mainForm.addRow(forgotPasswordLabel)
        mainForm.addRow(self.loginButton)
        mainForm.addRow(labelOR)
        mainForm.addRow(loginGoogleButton)

        mainLayout.addLayout(mainForm)

        notMemberLayout = QHBoxLayout()
        notMemberLayout.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        notMemberLabel = QLabel("Not a member?", self)
        notMemberLayout.addWidget(notMemberLabel)

        signUpButton = QPushButton("Register", self)
        signUpButton.setObjectName("LinkButton")
        signUpButton.setFlat(True)
        signUpButton.clicked.connect(self.onClickCreateNewUser)
        notMemberLayout.addWidget(signUpButton)

        mainLayout.addLayout(notMemberLayout)

    def onClickShowPasswordIfChecked(self, checked):
        if checked:
            self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif not checked:
            self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

    def onClickForgotPassword(self):
        print("To Forgot Password")

    def onClickLoginButton(self):
        self.loginIsSuccessful = True
        self.parent.nextScene(2)

    def onClickCreateNewUser(self):
        self.registerNewUser = True
        self.parent.nextScene(1)

    def openApplicationWindow(self):
        self.close()
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
        if self.loginIsSuccessful or self.registerNewUser:
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
