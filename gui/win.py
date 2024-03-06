"""
This module will store the window class
"""
from threading import Thread

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QProgressBar
)
from fcfs.sched import SchedulerFCFS
from PyQt6.QtCore import Qt

class MainWindow (QMainWindow):
    """Main window class

    Args:
        QMainWindow (class): Parent class
    """
    def __init__(self):
        super().__init__()
        self.setFixedSize(1_500, 300)
        self.timer = QTimer()
        self._main_widgets = {
            'upper': None,
            'lower': None,
        }
        self._c_ss_lst = [
            'yellow;',
            'green;',
            '#0a7091;'
        ]
        self._bttn_dict = {
            'halt': QPushButton('Halt'),
            'resume': QPushButton('Resume'),
        }
        self.sched = SchedulerFCFS({'p_count':15})

        self._set_main_widgets()
        self._set_main_w_color()

        self._set_buttons()
        self._set_labels()
        self._prog_bar_list = self._set_progbar_lst(15)
        self._add_pb_lst()
        self.thread_p = Thread(target=self.sched.run_queue)
        self.thread_p.start()
        self.timer.timeout.connect(self.update_state_bar)
        self.timer.start(100)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

    def update_state_bar(self):
        for bar, p_dict in self._prog_bar_list:
            bar.setValue(p_dict['cur_state'].value)
            self.update_bar_color(bar, p_dict)

    def update_bar_color(self, bar, p_dict):
        if p_dict['cur_state'].value < p_dict['p_fi_val']:
                if p_dict['p_halt'].value:
                    bar.setStyleSheet(f'QProgressBar::chunk {{ background-color: {self._c_ss_lst[0]};}} ')
                else:
                    bar.setStyleSheet(f'QProgressBar::chunk {{ background-color: {self._c_ss_lst[1]};}} ')
        else:
            bar.setStyleSheet(f'QProgressBar::chunk {{ background-color: {self._c_ss_lst[2]};}} ')

    def _add_pb_lst(self):
        for bar, _ in self._prog_bar_list:
            self._main_widgets['upper']['layout'].addWidget(bar)

    def _set_progbar_lst(self, amount):
        prg_barls = []
        self.sched.set_process_queue()
        for _ in range(amount):
            p_info_dict = self.sched.p_queue.get()

            bar = QProgressBar()
            bar.setRange(0, p_info_dict['p_fi_val'])
            bar.setOrientation(Qt.Orientation.Vertical)
            bar.setStyleSheet('QProgressBar {{border-radius: 10px;}}')

            self.sched.p_queue.put(p_info_dict)
            prg_barls.append((bar, p_info_dict))

        stp_str = self.sched.p_queue.get()
        self.sched.p_queue.put(stp_str)

        return prg_barls

    def _set_labels(self):
        label_container = QWidget()
        lbl_cont_layout = QHBoxLayout()
        label_container.setLayout(lbl_cont_layout)
        label_container.setFixedSize(300, 35)

        state_label = QLabel('State:')
        lbl_cont_layout.addWidget(state_label)

        self.spawn_label_list(lbl_cont_layout)

        self._main_widgets['lower']['layout'].addWidget(label_container)

    def spawn_label_list(self, layout):
        lbl_lst = [
            QLabel('Bloqued'),
            QLabel('Running'),
            QLabel('Finished')
        ]
        for index, label in enumerate(lbl_lst):
            label.setStyleSheet(f'color: {self._c_ss_lst[index]};')
            layout.addWidget(label)

    def _set_buttons(self):
        for value in self._bttn_dict.values():
            self._configure_bttns(value)
        self._configure_click_events()

    def _configure_click_events(self):
        self._bttn_dict['halt'].clicked.connect(self._halt_process)
        self._bttn_dict['resume'].clicked.connect(self._resume_process)

    def _configure_bttns(self, bttn):
        bttn.setStyleSheet('background-color: #72a19f;')
        self._main_widgets['lower']['layout'].addWidget(bttn)

    def _halt_process(self):
        self.sched.cur_p['p_halt'].value = True

    def _resume_process(self):
        self.sched.cur_p['p_halt'].value = False

    def setCentralWidget(self, widget: QWidget | None) -> None:
        central_layout = QVBoxLayout()

        widget.setLayout(central_layout)
        central_layout.addWidget(self._main_widgets['upper']['widget'])
        central_layout.addWidget(self._main_widgets['lower']['widget'])

        super().setCentralWidget(widget)

    def _set_main_widgets(self):
        """
        Sets window main widgets with their layouts
        """
        for key in self._main_widgets.keys():
            widget_dict = {
                'widget':QWidget(),
                'layout':QHBoxLayout() if key == 'upper' else QVBoxLayout()
            }
            widget_dict['widget'].setLayout(widget_dict['layout'])
            widget_dict
            self._main_widgets[key] = widget_dict

    def _set_main_w_color(self):
        self._main_widgets['upper']['widget'].setStyleSheet("""background-color: gray;
                                                              border-radius: 10px""")
        self._main_widgets['lower']['widget'].setStyleSheet("""background-color: darkgray;
                                                              border-radius: 10px""")
