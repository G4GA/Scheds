"""
GUI for Round Robin Scheduler
"""

from PyQt6.QtWidgets import (
    QProgressBar
)

from .sched_win import SchedulerWindow
from sched.rr import SchedulerRR

class WindowRR(SchedulerWindow):
    def __init__(self):
        super().__init__('Round Robin')
        self.sched_rr = SchedulerRR(arg_dict={'p_count': 15})
