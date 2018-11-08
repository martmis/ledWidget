import sys
from math import sqrt, pow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class LedMarti(QWidget):

    def __init__(self):
        super(LedMarti, self).__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Widget')
        self.ledIsOn = False
        self.initUI()

    def initUI(self):
        self.radius = 50
        self.center = QPoint(100,50)
        self.show()

    def on_click(self):
        if self.ledIsOn is False:
            self.ledIsOn = True
        else:
            self.ledIsOn = False
        self.repaint()

    # y goes down lol
    def mousePressEvent(self, event):
        x = int(event.x())
        y = int(event.y())

        cx = self.center.x() + 0.5*self.radius
        cy = self.center.y() + 0.5*self.radius

        # some calculations, move them to new method
        dist = sqrt(pow((x - cx),2)+ pow((y-cy),2))

        if dist < 0.5*self.radius:
            self.on_click()

    # radius can't be less than zero (absolute position of the widget, and can't be bigger than any of the dim)
    def resizeEvent(self, QResizeEvent):
        old_width = QResizeEvent.oldSize().width()
        old_height = QResizeEvent.oldSize().height()
        new_width = QResizeEvent.size().width()
        new_height = QResizeEvent.size().height()

        if old_width is not -1:
            wid_diff = new_width - old_width
            new_radius = self.radius + wid_diff
            if new_radius > 0:
                if new_radius <= new_width and new_radius <= new_height:
                    self.radius = self.radius + wid_diff
                else:
                    if new_radius > new_width:
                        self.radius = new_width
                    elif new_radius > new_height:
                        self.radius = new_height
            self.repaint()

        if old_height is not -1:
            hgt_diff = new_height - old_height
            if new_radius > 0:
                if new_radius <= new_width and new_radius <= new_height:
                    self.radius = self.radius + hgt_diff
                else:
                    if new_radius > new_width:
                        self.radius = new_width
                    elif new_radius > new_height:
                        self.radius = new_height
            self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.ledIsOn is False:
            qp.setPen(QPen(Qt.darkRed, 2, Qt.SolidLine))
            brush = QBrush()
            brush.setColor(Qt.red)
            brush.setStyle(Qt.Dense3Pattern)
            qp.setBrush(brush)
            qp.drawEllipse(self.center.x(), self.center.y(), self.radius, self.radius)

        else:
            qp.setPen(QPen(Qt.darkGreen, 2, Qt.SolidLine))
            brush = QBrush()
            brush.setColor(Qt.green)
            brush.setStyle(Qt.Dense3Pattern)
            qp.setBrush(brush)
            qp.drawEllipse(self.center.x(), self.center.y(), self.radius, self.radius)
        qp.end()


def main():
    app = QApplication(sys.argv)
    ex = LedMarti()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()