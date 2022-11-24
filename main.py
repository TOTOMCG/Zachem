import random
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randrange


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)

        self.paint = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)

            self.draw_circles(qp)

            qp.end()
        self.paint = False

    def draw_circles(self, qp):
        circle_amount = random.randrange(1, 10)
        qp.setBrush(QColor(255, 255, 0))
        for i in range(circle_amount):
            r = random.randrange(20, 100)
            qp.drawEllipse(random.randrange(50, 1000), random.randrange(50, 700), r, r)


app = QApplication(sys.argv)
ex = YellowCircles()
ex.show()
sys.exit(app.exec_())
