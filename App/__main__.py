import multiprocessing
import sys

from PyQt6.QtWidgets import QApplication
from dotenv import load_dotenv

from App.SceneManager import SceneManager
from Services.App import Startup

if __name__ == '__main__':
    # Take environment variables from .env
    load_dotenv()

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet("""
        QLabel#LoginTitle {
            color: #332F2E;
            font: bold 24px 'Monospace';
            margin: 12px 12px
        }
    
        QLineEdit {
            border: none;
            border-bottom: 1px solid #CCC;
            font: normal 13px 'Monospace';
            padding-right: 8px;
            padding-left: 8px;
            padding-top: 0px;
            padding-bottom: 10px;
            margin: 3px 8px;
        }
        
        QLineEdit:focus {
            border-bottom: 1px solid #5194FF;
        }
        
        QPushButton#LinkButton {
            color: #322CFF;
            font: bold 12px 'Monospace';
            padding-right: 8px;
            text-align: right;
        }
        
        QPushButton#LinkButton:pressed {
            background-color: white;
            border: none;
        }
        
        QPushButton#LoginGoogleButton {
            background-color: #CCC; 
            color: #332F2E;
            font: normal 12px 'Monospace';
            border-radius: 12px; 
            padding: 8px;
            margin: 12px; 
        }
        
        QPushButton#LoginButton {
            background-color: #3859FF; 
            color: white;
            font: bold 14px 'Monospace';
            border-radius: 12px; 
            padding: 8px;
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
    process = multiprocessing.Process(target=Startup)
    process.start()
    # Block the call to that the user exit of app
    code = app.exec()
    # Terminate the backend process
    process.terminate()
    # Close the app and cleanup resources
    sys.exit(code)
