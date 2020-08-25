import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pos_x = int(self.width() / 2)
        self.direction = 1
        self.speed = 10

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("QPaint~")

        self.timer = QTimer(self)
        self.timer.start(1000/30)
        self.timer.timeout.connect(self.timeout_run)

        btn = QPushButton('Quit', self)
        btn.move(self.width() / 2 - 40, self.height() / 2 + 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp):
        qp.setPen(QPen(Qt.blue, 10))
        qp.drawPoint(self.pos_x, self.height() / 2)

    def timeout_run(self):
        if self.pos_x < 10 or self.pos_x > self.width() - 10:
            self.direction *= -1
        self.pos_x = self.pos_x + (self.direction * self.speed)
        # print(self.pos_x, self.width())
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainW = Main()
    mainW.show()
    sys.exit(app.exec_())