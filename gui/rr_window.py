"""
GUI for Round Robin Scheduler
"""

from PyQt6.QtWidgets import (
    QProgressBar,
    QPushButton
)

from PyQt6.QtCore import QTimer

from .sched_win import SchedulerWindow
from sched.rr import SchedulerRR

class WindowRR(SchedulerWindow):
    def __init__(self):
        super().__init__('Round Robin')
        self._attributes['p_column_list'] = []
        self._attributes['timer'] = QTimer()
        self.sched_rr = SchedulerRR(arg_dict={'p_count': 15})

    @property
    def _timer(self) -> QTimer:
        return self._attributes['timer']

    @property
    def _column_list(self) -> list:
        return self._attributes['p_column_list']

    def _create_process_column(self):
        _, p_info_list = self.sched_rr.p_list
        for i in range(self.sched_rr.p_count):
            prog_bar = QProgressBar()
            column_dict = {
                'prog_bar': prog_bar,
                'halt_bttn': QPushButton('Halt'),
                'resume': QPushButton('Resume'),
                'restart': QPushButton('Restart')
            }
            prog_bar.setRange(0, p_info_list[i]['finished_state'])
            prog_bar.setValue(0)
            self._column_list.append(column_dict)

    def _add_progress_bar(self, progress_bar) -> None:
        self._upper['layout'].addWidget()