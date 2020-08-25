import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from mymodify.dice.user import User
from mymodify.menu import menu
from random import randint
from PyQt5.QtGui import *
from PyQt5 import QtCore
from mymodify.dice.game import Game

# qtDesigner로 화면 구성
CalUI = '../_guiFiles/frame_test2.ui'


class MainDialog(QDialog) :
    def __init__(self, game):
# 게임 화면
# ui 파일 불러오기 및 gui
# 넘어온 game객체 self.game으로 저장
        super(MainDialog, self).__init__()
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)
        self.setupUI()
        self.setFixedSize(800, 800)
        self.count = 0
        self.game = game

    def setupUI(self):

        self.btn1.clicked.connect(self.dice)


# 유저 주사위
    def dice(self):
# 유저 구분 idx, 회차 구분 count
        idx = self.count % self.game.persons
        self.count += 1
# 주사위 버튼 시 메서드( game 변수목록 클래스, 회차 cnt, 1번째 2번째 유저 구분여부 idx)
        result = self.game.users[idx].dice(self.game, self.count, idx)

        if idx == 0 :
        ## 이미지 표시 ( 3차원 배열 )
            self.player1.setGeometry(self.game.land[idx][self.game.users[idx].land_idx][0],
                                     self.game.land[idx][self.game.users[idx].land_idx][1],
                                     self.game.land[idx][self.game.users[idx].land_idx][2],
                                     self.game.land[idx][self.game.users[idx].land_idx][3]
                                     )

            self.main_text.setPlainText("{}의 주사위 {} !!!".format(self.game.users[idx].name,result))
            self.player1_text.append("{}만큼 이동!! 현재 위치는 land[{}]입니다.".format(result, self.game.users[idx].land_idx))
        elif idx == 1:
            self.player2.setGeometry(self.game.land[idx][self.game.users[idx].land_idx][0],
                                     self.game.land[idx][self.game.users[idx].land_idx][1],
                                     self.game.land[idx][self.game.users[idx].land_idx][2],
                                     self.game.land[idx][self.game.users[idx].land_idx][3]
                                     )
            self.main_text.setPlainText("{}의 주사위 {} !!!".format(self.game.users[idx].name,result))
            self.player2_text.append("{}만큼 이동!! 현재 위치는 land[{}]입니다.".format(result, self.game.users[idx].land_idx))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainDialog = MainDialog()
    mainDialog.show()
    app.exec_()
