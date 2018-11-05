import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Widget')
        self.ledIsOn = False
        self.button = QPushButton()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Widget')
        self.button = QPushButton('pressme', self)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        if self.ledIsOn is False:
            self.ledIsOn = True
        else:
            self.ledIsOn = False
        self.repaint()

    def resizeEvent(self, QResizeEvent):
        old_width = QResizeEvent.oldSize().width()
        old_height = QResizeEvent.oldSize().height()
        new_width = QResizeEvent.size().width()
        new_height = QResizeEvent.Size().heigth()


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.ledIsOn is False:
            qp.setPen(Qt.SolidLine)
            qp.setBrush(Qt.red)
            qp.drawEllipse(100, 50, 50, 50)
        else:
            qp.setPen(QColor(Qt.black))
            qp.setBrush(Qt.darkGreen)
            qp.drawEllipse(100, 50, 50, 50)
        qp.end()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()