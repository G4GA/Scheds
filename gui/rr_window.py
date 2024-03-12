"""
GUI for Round Robin Scheduler
"""

from PyQt6.QtWidgets import (
    QPushButton,
    QProgressBar,
    QVBoxLayout,
    QWidget
)

from PyQt6.QtCore import QTimer
from PyQt6 import QtCore

from .sched_win import SchedulerWindow
from sched.rr import SchedulerRR

class WindowRR(SchedulerWindow):
    def __init__(self):
        super().__init__('Round Robin')
        self._attributes['p_column_list'] = []
        self._attributes['timer'] = QTimer()

        self.sched_rr = SchedulerRR(arg_dict={'p_count': 15})
        self.sched_rr._build_process()
        self._create_process_column()

        self._set_timer()
        self._timer.start(100)
        self.sched_rr.run()

    @property
    def _prog_bar_list(self):
        return [prog_bar for prog_bar, _ in self._column_list]

    @property
    def _process_list(self):
        return [process for _, process in self.sched_rr.p_list]

    @property
    def _p_info_list(self):
        return [p_info for _, p_info in self.sched_rr.p_list]

    @property
    def _timer(self) -> QTimer:
        return self._attributes['timer']

    @property
    def _column_list(self) -> list:
        return self._attributes['p_column_list']

    def _create_process_column(self):
        for index in range(self.sched_rr.p_count):
            prog_bar = QProgressBar()
            button_dict = {
                'halt': QPushButton('Halt'),
                'resume': QPushButton('Resume'),
                'restart': QPushButton('Restart')
            }
            self._set_prog_bar(index, prog_bar)
            self._add_prog_bar(prog_bar)

            self._add_buttons(button_dict)
            self._set_button_callbacks(index, button_dict)

            self._column_list.append([prog_bar, button_dict])

    def _set_prog_bar(self, index, prog_bar:QProgressBar):
        prog_bar.setRange(0, self._p_info_list[index]['finished_state'].value)
        prog_bar.setValue(0)
        prog_bar.setFixedHeight(240)
        prog_bar.setOrientation(QtCore.Qt.Orientation.Vertical)
        prog_bar.setStyleSheet('''QProgressBar::chunk {background-color: #76d955}''')

    def _set_timer(self):
        self._timer.timeout.connect(self.update_progress_bar)

    def update_progress_bar(self):
        for index, prog_bar in enumerate(self._prog_bar_list):
            prog_bar.setValue(self._p_info_list[index]['cur_state'].value)
            if not self.sched_rr.p_list[index][0].is_alive():
                prog_bar.setStyleSheet('''QProgressBar::chunk {
                                                background-color: #5597d9;
                                                border-radius: 10px
                                                }''')

    def _set_button_callbacks(self, index:int, button_dict:dict):
        button_dict['halt'].clicked.connect(lambda: self.halt_process(index))
        button_dict['resume'].clicked.connect(lambda: self.resume_process(index))
        button_dict['restart'].clicked.connect(lambda: self.restart_process(index))

    def _add_buttons(self, button_dict):
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)

        for _, value in button_dict.items():
            layout.addWidget(value)

        self._lower['layout'].addWidget(widget)

    def _add_prog_bar(self, prog_bar):
        self._upper['layout'].addWidget(prog_bar)

    def halt_process(self, index):
        if self.sched_rr.p_list[index][0].is_alive():
            self._p_info_list[index]['halt'].value = True
            self._prog_bar_list[index].setStyleSheet('''QProgressBar::chunk {background-color: #e8d73a}''')

    def resume_process(self, index):
        if self.sched_rr.p_list[index][0].is_alive():
            self._p_info_list[index]['halt'].value = False
            self._prog_bar_list[index].setStyleSheet('''QProgressBar::chunk {background-color: #76d955}''')

    def restart_process(self, index):
        if self.sched_rr.p_list[index][0].is_alive():
            self._p_info_list[index]['cur_state'].value = 0