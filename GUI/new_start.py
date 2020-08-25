import sys
from PyQt5.QtWidgets import *
from mymodify.GUI.setting import SettingBase


# 첫번째 화면 시작하기, 선택하면 두번째 화면 실행
class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        btn1 = QPushButton('1.시작하기', self)
        btn1.move(150, 100)
        btn1.clicked.connect(self.pushButton1)

        btn2 = QPushButton('2.불러오기', self)
        btn2.move(150, 150)
        btn2.clicked.connect(self.pushButton2)

        btn3 = QPushButton('3.나가기  ', self)
        btn3.move(150, 200)
        btn3.clicked.connect(self.pushButton3)

        self.setWindowTitle("Random Dice")
        self.setGeometry(700, 500, 400, 300)
        self.setFixedSize(400, 300)

    def pushButton1(self):
        set = SettingBase()
        set.exec_()

    def pushButton2(self):
        pass

    def pushButton3(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = FirstWindow()
    start.show()
    app.exec_()
