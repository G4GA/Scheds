"""
This module will store the window class
"""
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QWidget
)

class MainWindow (QMainWindow):
    """Main window class

    Args:
        QMainWindow (class): Parent class
    """
    def __init__(self):
        super().__init__()