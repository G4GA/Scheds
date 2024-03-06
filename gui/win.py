"""
This module will store the window class
"""
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)

from copy import deepcopy

class MainWindow (QMainWindow):
    """Main window class

    Args:
        QMainWindow (class): Parent class
    """
    def __init__(self):
        super().__init__()
        self.setFixedSize(1_500, 500)

        self.main_widgets = {
            'upper': None,
            'lower': None,
        }
        self._set_main_widgets()
        self.set_main_w_color()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

    def setCentralWidget(self, widget: QWidget | None) -> None:
        central_layout = QVBoxLayout()

        widget.setLayout(central_layout)
        central_layout.addWidget(self.main_widgets['upper']['widget'])
        central_layout.addWidget(self.main_widgets['lower']['widget'])

        super().setCentralWidget(widget)

    def _set_main_widgets(self):
        """
        Sets window main widgets with their layouts
        """
        for key, _ in self.main_widgets.items():
            widget_dict = {
                'widget':QWidget(),
                'layout':QHBoxLayout()
            }
            widget_dict['widget'].setLayout(widget_dict['layout'])
            widget_dict
            self.main_widgets[key] = widget_dict

    def set_main_w_color(self):
        self.main_widgets['upper']['widget'].setStyleSheet("""background-color: gray;
                                                              border-radius: 10px""")
        self.main_widgets['lower']['widget'].setStyleSheet("""background-color: lightgray;
                                                              border-radius: 10px""")
