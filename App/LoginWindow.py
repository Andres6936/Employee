from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QCloseEvent
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox, QVBoxLayout, \
    QFormLayout

from App.MainWindow import MainWindow
from App.Scene.ISceneManager import ISceneManager
from App.Services.Connector import Connector


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

        self.connector = Connector()

        self.usernameText = ""
        self.passwordText = ""

        self.setFixedSize(375, 667)
        self.setWindowTitle("Login")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        mainLayout = QVBoxLayout(self)

        loginLabel = QLabel("Login")
        loginLabel.setFont(QFont("Arial", 20))
        loginLabel.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        mainLayout.addWidget(loginLabel)

        usernameEdit = QLineEdit(self)
        usernameEdit.textChanged.connect(self.onTextChangedUsername)

        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEdit.textChanged.connect(self.onTextChangedPassword)

        showPasswordCheckbox = QCheckBox("Show Password", self)
        showPasswordCheckbox.toggled.connect(self.onClickShowPasswordIfChecked)

        self.loginButton = QPushButton("Login", self)
        self.loginButton.setEnabled(False)
        self.loginButton.setStyleSheet("""
            background-color: #3859FF; 
            color: white;
            font: bold 14px 'Monospace';
            border-radius: 12px; 
            padding: 5px;
            margin: 12px; 
        """)
        self.loginButton.clicked.connect(self.onClickLoginButton)

        mainForm = QFormLayout()
        mainForm.setFieldGrowthPolicy(mainForm.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        mainForm.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        mainForm.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        mainForm.addRow("Username", usernameEdit)
        mainForm.addRow("Password", self.passwordEdit)
        mainForm.addRow(showPasswordCheckbox)
        mainForm.addRow(self.loginButton)

        mainLayout.addLayout(mainForm)

        notMemberLabel = QLabel("Not a member?", self)
        notMemberLabel.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
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
