# import sys

# from PySide6.QtGui import QGuiApplication
# from PySide6.QtQml import QQmlApplicationEngine


# app = QGuiApplication(sys.argv)

# engine = QQmlApplicationEngine()
# engine.quit.connect(app.quit)
# engine.load('main.qml')

# sys.exit(app.exec_())
import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

sys.exit(app.exec())