"""
GUI for FCFS schduler
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from .sched_win import SchedulerWindow

class WindowFCSF(SchedulerWindow):
    def __init__(self):
        super().__init__()