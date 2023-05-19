from PySide2.QtWidgets import QApplication, QMainWindow

from MainWindow import MainWindow

app = QApplication([])

main_window = QMainWindow()

ui = MainWindow()
ui.setupUi(main_window)

main_window.show()

app.exec_()
