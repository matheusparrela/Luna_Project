from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from MainWindow import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = MainWindow()
    ui.setupUi(main_window)
    main_window.show()

    sys.exit(app.exec_())
