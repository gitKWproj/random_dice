import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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
        self.btn1.pressed.connect(self.dice_roll_on)
        self.btn1.clicked.connect(self.dice)

    # 버튼 눌린상태일때 주사위 돌아가는 gif
    def dice_roll_on(self):
        self.movie = QMovie("../_image/dice_roll.gif")
        self.label_3.setMovie(self.movie)
        self.movie.setSpeed(1000)
        self.movie.start()

    # 버튼 클릭될때, 유저 주사위
    def dice(self):
        # 유저 구분 idx, 회차 구분 count
        idx = self.count % self.game.persons
        self.count += 1

        # 주사위 버튼 시 메서드( game 변수목록 클래스, 회차 cnt, 1번째 2번째 유저 구분여부 idx)
        result = self.game.users[idx].dice(self.game, self.count, idx)

        # gif 멈추고, gif 대신 해당 주사위 숫자 표시, 버튼 클릭 불가능, 주사위 갯수 텍스트 표시
        self.movie.stop()
        self.label_3.setPixmap(QtGui.QPixmap("../_image/%d.png" % result))
        self.btn1.setEnabled(False)
        self.main_text.setPlainText("{}의 주사위 {} !!!".format(self.game.users[idx].name, result))

        # 각 플레이어 이동 이미지 변경, 각 현재 땅 출력
        if idx == 0 :
            self.player1.setPixmap(QtGui.QPixmap("../_image/player1_test.png"))
            self.player1_text.append("{}만큼 이동!! 현재 위치는 land[{}]입니다.".format(result, self.game.users[idx].land_idx))
        elif idx == 1:
            self.player2.setPixmap(QtGui.QPixmap("../_image/player2_test.png"))
            self.player2_text.append("{}만큼 이동!! 현재 위치는 land[{}]입니다.".format(result, self.game.users[idx].land_idx))

        # 이동 이미지 부드럽게 이동 timer
        self.timer = QTimer(self)
        self.timer.start(1 / 10000)
        self.timer.timeout.connect(self.timeout_run)

    # 실시간 이미지 좌표 그리기
    def paintEvent(self, e):
        idx = (self.count-1) % self.game.persons
        if idx == 0: self.draw_point(self.player1)
        elif idx == 1: self.draw_point(self.player2)

    #
    def draw_point(self, qp):
        idx = (self.count-1) % self.game.persons
        qp.setGeometry(self.game.users[idx].virtual_x,
                           self.game.users[idx].virtual_y,
                           self.game.land[idx][self.game.users[idx].land_idx][2],
                           self.game.land[idx][self.game.users[idx].land_idx][3])

    def timeout_run(self):
        idx = (self.count-1) % self.game.persons

        if self.game.users[idx].virtual_idx == self.game.users[idx].land_idx:
            if idx == 0: self.player1.setPixmap(QtGui.QPixmap("../_image/player1_resize.png"))
            elif idx == 1: self.player2.setPixmap(QtGui.QPixmap("../_image/player2_resize.png"))
            self.btn1.setEnabled(True)
            self.timer.stop()
        else:
            if self.game.users[idx].virtual_idx < 5:
                self.game.users[idx].virtual_x -= 1
                if self.game.land[idx][self.game.users[idx].virtual_idx+1][0] == self.game.users[idx].virtual_x:
                    self.game.users[idx].virtual_idx += 1

            elif 5 <= self.game.users[idx].virtual_idx & self.game.users[idx].virtual_idx < 9:
                self.game.users[idx].virtual_y -= 1
                if self.game.land[idx][self.game.users[idx].virtual_idx+1][1] == self.game.users[idx].virtual_y:
                    self.game.users[idx].virtual_idx += 1

            elif 9 <= self.game.users[idx].virtual_idx & self.game.users[idx].virtual_idx < 14:
                self.game.users[idx].virtual_x += 1
                if self.game.land[idx][self.game.users[idx].virtual_idx+1][0] == self.game.users[idx].virtual_x:
                    self.game.users[idx].virtual_idx += 1

            elif 14 <= self.game.users[idx].virtual_idx & self.game.users[idx].virtual_idx < 17:
                self.game.users[idx].virtual_y += 1
                if self.game.land[idx][self.game.users[idx].virtual_idx+1][1] == self.game.users[idx].virtual_y:
                    self.game.users[idx].virtual_idx += 1

            elif self.game.users[idx].virtual_idx == 17:
                self.game.users[idx].virtual_y += 1
                if self.game.land[idx][0][1] == self.game.users[idx].virtual_y:
                    self.game.users[idx].virtual_idx = 0
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainDialog = MainDialog()
    mainDialog.show()
    app.exec_()
