import sys
from PySide2.QtCore import QSize, Qt
from  PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first app")
        button = QPushButton("clique aqui!")

        self.setFixedSize(QSize(400,300))

        self.setCentralWidget(button)

        button.clicked.connect(self.print_result)

    def print_result(self):

        print("botão clicado")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
