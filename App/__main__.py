import sys

from PyQt6.QtGui import QFont, QCloseEvent
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox

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

        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEdit.resize(250, 24)
        self.passwordEdit.move(90, 82)

        showPasswordCheckbox = QCheckBox("Show Password", self)
        showPasswordCheckbox.move(90, 110)
        showPasswordCheckbox.toggled.connect(self.onClickShowPasswordIfChecked)

        loginButton = QPushButton("Login", self)
        loginButton.resize(320, 24)
        loginButton.move(20, 140)
        loginButton.clicked.connect(self.onClickLoginButton)

        notMemberLabel = QLabel("Not a member?", self)
        notMemberLabel.move(20, 186)

        signUpButton = QPushButton("Sign Up", self)
        signUpButton.move(120, 180)
        signUpButton.clicked.connect(self.onClickCreateNewUser)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
