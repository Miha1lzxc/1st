from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType(" UI.ui")


class Window(QMainWindow):
    def __init__(self):
        self.should_paint_circle = False

    self.btn.clicked.connect(self.paintcircle)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            painter = QtGui.QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
            painter.drawEllipse(100, 100, 100, 100)

    def paintcircle(self):
        self.should_paint_circle = True
        self.update()


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
