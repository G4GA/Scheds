import sys
from PyQt6.QtWidgets import QApplication
from gui.initial_window import InitialWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = InitialWindow()
    main_window.show()

    app.exec()
