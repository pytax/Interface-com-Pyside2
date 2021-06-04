from PySide2.QtWidgets import QApplication, QWidget

import sys

#você precisa de apenas uma instancia por aplicação
app = QApplication(sys.argv)
#criação do qtwidget que será a janela
window = QWidget()
#começa o evento loop
window.show()

app.exec_()
