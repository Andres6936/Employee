import sys

from PyQt6.QtWidgets import QApplication
from dotenv import load_dotenv

from App.SceneManager import SceneManager

if __name__ == '__main__':
    # Take environment variables from .env
    load_dotenv()

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet("""
        QLineEdit {
            border: 1px solid #CCC;
            border-radius: 12px;
            padding: 3px 5px;
        }
        
        QLineEdit:focus {
            border: 2px solid #5194FF;
        }
        
        QPushButton#LoginButton {
            background-color: #3859FF; 
            color: white;
            font: bold 14px 'Monospace';
            border-radius: 12px; 
            padding: 5px;
            margin: 12px; 
        }
         
         QPushButton#LoginButton:hover {
            background-color: #5194FF; 
        }
            
        QPushButton#LoginButton:pressed {
            background-color: #322CFF;
        }
            
        QPushButton#LoginButton:disabled {
            background-color: #6BC4FF; 
        }
    """)
    window = SceneManager()
    sys.exit(app.exec())
