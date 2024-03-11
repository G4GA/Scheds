"""
Parent class for scheduler window
"""

from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

class SchedulerWindow(QMainWindow):
    def __init__(self, window_name:str):
        super().__init__()
        self._attributes = {
            'main_widgets': {
                'upper': {
                    'widget': QWidget(),
                    'layout': QHBoxLayout()
                },
                'lower': {
                    'widget': QWidget(),
                    'layout': QHBoxLayout()
                }
            },
            'central_widget': {
                'widget': QWidget(),
                'layout': QVBoxLayout()
            }
        }
        self._initialize_window(window_name)
        self.setCentralWidget(self._central_widget['widget'])

    @property
    def _upper(self):
        return self._attributes['main_widgets']['upper']

    @property
    def _lower(self):
        return self._attributes['main_widgets']['lower']

    @property
    def _central_widget(self) -> QWidget:
        return self._attributes['central_widget']

    def _initialize_window(self, window_name):
        name = 'Invalid name'
        if isinstance(window_name, str):
            name = window_name

        self.setWindowTitle(name)
        self.setFixedSize(1_000, 500)

        self._central_widget['widget'].setLayout(self._central_widget['layout'])
        self._set_ul_widgets()
        self._style_main_widget()

    def _set_ul_widgets(self):
        self._upper['widget'].setLayout(self._upper['layout'])
        self._central_widget['layout'].addWidget(self._upper['widget'])
        self._lower['widget'].setLayout(self._lower['layout'])
        self._central_widget['layout'].addWidget(self._lower['widget'])

    def _style_main_widget(self):
        style_sheet = open('./style.css').read()
        self._upper['widget'].setObjectName('upper')
        self._lower['widget'].setObjectName('lower')
        self.setStyleSheet(style_sheet)