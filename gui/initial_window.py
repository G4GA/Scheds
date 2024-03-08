"""
This module will store a class that will show
the initial menu window.
"""

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)

from .fcfs_win import WindowFCSF
from .rr_window import WindowRR

class InitialWindow(QMainWindow):
    """
    Menu for calling opening a scheduler
    """
    def __init__(self):
        super().__init__()
        self._set_window()
        self.__attributes = {
            'main_layout': {
                'upper': {},
                'lower': {}
            },
            'central_widget':QWidget(),
            'new_window': None
        }
        self._set_main_layout()
        self._add_label()
        self._add_bttns()
        self.setCentralWidget(self.__attributes['central_widget'])

    def _open_window(self, constructor):
        """
        Calls window constructor and shows window object

        Args:
            constructor (callback): constructor of the window class
        """
        self._new_window = constructor()
        self._new_window.show()

        self.close()

    def _add_bttns(self):
        """
        Adds buttons for opening windows
        """
        bttn_info = [
            ('FCFS', WindowFCSF),
            ('Round Robin', WindowRR)
        ]
        for label, construct in bttn_info:
            self._create_button(label, construct)

    def _create_button(self, label:str, constr_callback):
        """
        Initializes and sets window button

        Args:
            label (str): Button label
            constr_callback (callback): Window class constructor
        """
        bttn = QPushButton(label)
        bttn.clicked.connect(lambda: self._open_window(constr_callback))
        self._lower['layout'].addWidget(bttn)

    def _add_label(self):
        """
        Adds the welcome label
        """
        menu_label = QLabel('Welcome!\nSelect one of the following options:')
        self._upper['layout'].addWidget(menu_label)

    def setCentralWidget(self, widget: QWidget | None) -> None:
        """
        Sets central widget layout and appends it to the window
        """
        layout = QVBoxLayout()
        widget.setLayout(layout)

        layout.addWidget(self._upper['widget'])
        layout.addWidget(self._lower['widget'])

        return super().setCentralWidget(widget)

    @property
    def _main_layout(self):
        """
        Returns main_layout
        """
        return self.__attributes['main_layout']

    @property
    def _upper(self) -> dict:
        """
        Returns upper dict
        """
        return self._main_layout['upper']

    @property
    def _lower(self) -> dict:
        """
        Returns lower dict
        """
        return self._main_layout['lower']

    @property
    def _new_window(self):
        """
        Returns new_window object
        """
        return self.__attributes['new_window']

    @_new_window.setter
    def _new_window(self, window):
        """
        Sets new_window object
        """
        self.__attributes['new_window'] = window

    def _set_main_layout(self):
        """
        Sets main_layout
        """
        self._init_layout('upper')
        self._init_layout('lower')

    def _init_layout(self, key):
        """
        Creates and initializes layout
        """
        widget = QWidget()
        layout = QHBoxLayout()
        self._main_layout[key] = {
            'widget': widget,
            'layout': layout
        }
        widget.setLayout(layout)

    def _set_window(self):
        """
        Sets window display properties
        """
        self.setFixedHeight(150)
        self.setWindowTitle("Menu")
