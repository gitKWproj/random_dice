import sys
from PyQt5.QtWidgets import *
from GUI.play import MainDialog
from dice.game import Game
from PyQt5.QtGui import QIcon

# 두번째 윈도우창 인원 수, 생명 설정창.

class SettingBase(QDialog):
    def __init__(self):
        super().__init__()
# ui파일 불러오기 및 gui
# 게임 진행에 필요한 Game클래스를 만들어서 변수목록들 저장
        self.setupUI()
        self.game = Game()

    def setupUI(self):
        self.setFixedSize(400, 300)
        self.setGeometry(1110, 500, 400, 300)
        self.setWindowTitle("설정")
        self.setWindowIcon(QIcon('../_image/dice_roll.gif'))

        label1 = QLabel("플레이어 1: ")
        label2 = QLabel("플레이어 2: ")
        label3 = QLabel("라이프 : ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.pushButton1 = QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)

        self.setLayout(layout)

# '등록' 버튼 클릭 이벤트a
    def pushButtonClicked(self):
        # lineEdit으로 값을 받으면 str형태로 저장
        self.game.start_life = int(self.lineEdit3.text())
        self.game.input_name(self.lineEdit1.text(), self.lineEdit2.text())
        self.close()
        # play.py의 클래스 3번째 윈도우 - 게임화면 (game - 게임에 필요한 변수들의 객체)
        dlg = MainDialog(self.game)
        dlg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    set = SettingBase()
    set.show()
    app.exec_()
