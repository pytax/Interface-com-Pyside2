from PySide2.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()
app.exec_()
