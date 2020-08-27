import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from dice.game import Game
# from GUI.result import ResultScreen

# qtDesigner로 화면 구성
CalUI = '../_guiFiles/frame_test2.ui'


class MainDialog(QDialog):
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
        self.last_text = ""

    def setupUI(self):

        # self.main_text 에는 27의 문자가 최대
        # self.main_text.setPlainText("{:^33}".format("랜덤 다이스 게임 시작!."))
        self.main_text.setPlainText(("랜덤 다이스 게임 시작!.").center(24, "*"))
        self.btn1.clicked.connect(self.dice)

    # User 클래스의 dice 함수를 호출해서 users[0] 과 users[1] 객체를 생성
    def dice(self):
        # 유저 구분 idx, 회차 구분 count
        idx = self.count % self.game.persons  # 0 or 1
        self.count += 1
        # 주사위 버튼 시 메서드( game 변수목록 클래스, 회차 cnt, 1번째 2번째 유저 구분여부 idx)
        result = self.game.users[idx].dice(self.game, self.count, idx)

        if idx == 0:
            ## 이미지 표시 ( 3차원 배열 )
            self.player1.setGeometry(self.game.land[idx][self.game.users[idx].land_idx][0],
                                     self.game.land[idx][self.game.users[idx].land_idx][1],
                                     self.game.land[idx][self.game.users[idx].land_idx][2],
                                     self.game.land[idx][self.game.users[idx].land_idx][3]
                                     )
            ## 땅이 비어있으면 점령, 남에 땅이면 life - 1
            #  land_idx = self.game.users[idx].land_idx
            self.game.game_process(self.game.users[idx].land_idx, idx)
            print(self.game.total_land)
            #  QTextBrowser인 main_text player1_text에 데이터 출력
            self.main_text.setPlainText(self.game.main_text)
            self.player1_text.append(self.game.users_text)
            # self.land_text.setPlainText(self.game.total_land)

        elif idx == 1:
            self.player2.setGeometry(self.game.land[idx][self.game.users[idx].land_idx][0],
                                     self.game.land[idx][self.game.users[idx].land_idx][1],
                                     self.game.land[idx][self.game.users[idx].land_idx][2],
                                     self.game.land[idx][self.game.users[idx].land_idx][3]
                                     )

            ## 땅이 비어있으면 점령, 남에 땅이면 life - 1
            self.game.game_process(self.game.users[idx].land_idx, idx)
            print(self.game.total_land)

            self.main_text.setPlainText(self.game.main_text)
            self.player2_text.append(self.game.users_text)

        print(self.game.users[idx].name, self.game.users[idx].life)
        # users의 life가 0이 되었을 때 dice 버튼 비활성화 last_text 출력
        if self.game.users[idx].life == 0:
            self.last_text = "{}님 땅을 {}개 점령하셨지만 패배하였습니다..".format(self.game.users[idx].name,
                                                                  self.game.total_land.count(self.game.users[idx].name))
            self.main_text.setPlainText(self.last_text)
            self.btn1.setEnabled(False)
            # self.result_screen()

    # def result_screen(self):
    #     win = ResultScreen()
    #     win.result_text.setPlainText(self.last_text)
    #     win.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game.start_life = 3
    game.input_name("Red", "Blue")
    mainDialog = MainDialog(game)
    mainDialog.show()
    app.exec_()

# self.game.start_life = self.lineEdit3.text()
# self.game.input_name(self.lineEdit1.text(), self.lineEdit2.text())
