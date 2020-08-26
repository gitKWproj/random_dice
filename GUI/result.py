import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton
from PyQt5 import QtWidgets
from GUI.setting import SettingBase

class ResultScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setWindowTitle('Radon_dice 결과')
        self.setGeometry(300, 300, 500, 400)

        self.result_text = QtWidgets.QTextBrowser(self)
        self.result_text.setGeometry(100, 100, 300, 200)

        btn1 = QPushButton("처음으로", self)
        btn1.setGeometry(100, 350, 100, 30)
        # btn1.clicked.connect(self.pushButton1)

        btn2 = QPushButton("나가기", self)
        btn2.setGeometry(300, 350, 100, 30)
        btn2.clicked.connect(self.pushButton2)

    # def pushButton1(self):
    #     fw = FirstWindow(self)
    #     fw.exec_()
    def pushButton2(self):
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = ResultScreen()
    screen.show()
    sys.exit(app.exec_())