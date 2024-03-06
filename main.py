import sys
from PyQt6.QtWidgets import QApplication
from gui.win import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
