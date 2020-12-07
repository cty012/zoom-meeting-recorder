from PyQt5.QtWidgets import QApplication
import sys

from window import MainWindow


app = QApplication(sys.argv)
app.setStyle('Fusion')
# app.setStyleSheet('QTabBar::tab { height: 100px; width: 100px; }')

window = MainWindow()
window.show()

sys.exit(app.exec_())
