import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from dice.game import Game



# qtDesigner로 화면 구성
CalUI = '../_guiFiles/frame_test2.ui'


class MainDialog(QDialog, QWidget):
    from test import Bigtext
    big = Bigtext(0)
    ending_text = big.show_text()
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

            # 빈땅이여서, True 일때만 색을 변경한다.
            if self.game.empty:                    # 해당 유저의 땅 번호, 고유색깔
                self.land_background_color(self.game.users[idx].land_idx, "red")
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

            # 빈땅이여서, True 일때만 색을 변경한다.
            if self.game.empty:                    # 해당 유저의 땅 번호, 고유색깔
                self.land_background_color(self.game.users[idx].land_idx, "blue")
            #  QTextBrowser인 main_text player2_text에 데이터 출력
            self.main_text.setPlainText(self.game.main_text)
            self.player2_text.append(self.game.users_text)


        # users의 life가 0이 되었을 때 dice 버튼 비활성화, last_text 출력, QMessageBox 이벤트 발생
        if self.game.users[idx].life == 0:
            self.last_text = "{}님 땅을 {}개 점령하셨지만 패배하였습니다.. \n 너가 아이스크림 쏘세요".format(self.game.users[idx].name,
                                                                  self.game.total_land.count(self.game.users[idx].name))
            self.main_text.setPlainText(self.last_text)
            self.btn1.setEnabled(False)

            # last_text를 전달해서 창에 띄운다.
            self.result_event(self.last_text, self.ending_text)
            # QMessageBox.about(self, "결과", self.last_text)

    # num = 해당유저의 땅번호, color = 해당유저의 고유 색깔
    def land_background_color(self, num, color):
        if num == 1:
            self.land_01.setStyleSheet("background: {}".format(color))
        elif num == 2:
            self.land_02.setStyleSheet("background: {}".format(color))
        elif num == 3:
            self.land_03.setStyleSheet("background: {}".format(color))
        elif num == 4:
            self.land_04.setStyleSheet("background: {}".format(color))
        elif num == 5:
            self.land_05.setStyleSheet("background: {}".format(color))
        elif num == 6:
            self.land_06.setStyleSheet("background: {}".format(color))
        elif num == 7:
            self.land_07.setStyleSheet("background: {}".format(color))
        elif num == 8:
            self.land_08.setStyleSheet("background: {}".format(color))
        elif num == 9:
            self.land_09.setStyleSheet("background: {}".format(color))
        elif num == 10:
            self.land_10.setStyleSheet("background: {}".format(color))
        elif num == 11:
            self.land_11.setStyleSheet("background: {}".format(color))
        elif num == 12:
            self.land_12.setStyleSheet("background: {}".format(color))
        elif num == 13:
            self.land_13.setStyleSheet("background: {}".format(color))
        elif num == 14:
            self.land_14.setStyleSheet("background: {}".format(color))
        elif num == 15:
            self.land_15.setStyleSheet("background: {}".format(color))
        elif num == 16:
            self.land_16.setStyleSheet("background: {}".format(color))
        elif num == 17:
            self.land_17.setStyleSheet("background: {}".format(color))

    # QMessageBox 실행
    def result_event(self, last_text, ending_text):
        reAlert = QMessageBox.question(self, '결과', "{0} \n{1}".format(ending_text, last_text), QMessageBox.Yes | QMessageBox.Cancel)


        if reAlert == QMessageBox.Yes:
            import webbrowser
            url = "http://www.baskinrobbins.co.kr/menu/list.php?top=A"
            webbrowser.open_new(url)
            self.close()
        elif reAlert == QMessageBox.Cancel:
            self.close()
            from GUI.setting import SettingBase
            dlg = SettingBase()
            dlg.exec_()


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