from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt6 Test Window")
window.resize(400, 300)
window.show()

app.exec()
