from PyQt5 import uic, QtGui
from GUI.rule import *

# qtDesigner로 화면 구성
CalUI = '../_guiFiles/frame_test2.ui'
ruleUI = '../_guiFiles.rule.ui'


class MainDialog(QDialog) :
    from test1 import Bigtext
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
        self.rule_dialog = Rule_dialog


    def setupUI(self):
        # self.main_text 에는 27의 문자가 최대
        # self.main_text.setPlainText("{:^33}".format("랜덤 다이스 게임 시작!."))
        self.main_text.setPlainText(("랜덤 다이스 게임 시작!.").center(24, "*"))
        self.btn1.pressed.connect(self.dice_roll_on)
        self.btn1.clicked.connect(self.dice)
        self.rule.clicked.connect(self.rule_btn)
        self.movie = QMovie("../_image/dice_roll.gif")
        self.setWindowIcon(QIcon('../_image/dice_roll.gif'))

    def rule_btn(self):
        Rul = Rule_dialog()
        Rul.exec_()

    # 버튼 눌린상태일때 주사위 돌아가는 모션( gif )
    def dice_roll_on(self):
        self.label_3.setMovie(self.movie)
        self.movie.setSpeed(1000)
        self.movie.start()

    # 버튼 클릭될때, 유저 주사위
    def dice(self):
        # 유저 구분 idx, 회차 구분 count
        idx = self.count % self.game.persons
        self.count += 1

        # 실제위치 메서드( game 변수목록 클래스, 회차 cnt, 1번째 2번째 유저 구분여부 idx)  - 실제위치
        result = self.game.users[idx].dice(self.game, self.count, idx)

        # gif 멈추고, gif 대신 해당 주사위 숫자 표시, 버튼 클릭 불가능, 주사위 갯수 텍스트 표시
        # 각 플레이어 이동 이미지 변경, 각 현재 땅 출력
        self.movie.stop()
        self.label_3.setPixmap(QtGui.QPixmap("../_image/%d.png" % result))
        # 무인도일때 메인 text
        if len(self.game.users[idx].countdown) > 0:
            self.main_text.setPlainText("돛단배 제작중..")
        else:
            self.main_text.setPlainText("{}의 주사위 {} !!!".format(self.game.users[idx].name, result))


        # 무인도에 들어갔을때 실행
        if len(self.game.users[idx].countdown) > 0:
            if idx == 0:
                self.game.specialplace1(idx)
                self.player1_text.append(self.game.users_text)
            # if 문으로 나눈 이유는 player_text를 각자 상황에 맞게 실행하기 위해 나눔
            elif idx == 1:
                self.game.specialplace1(idx)
                self.player2_text.append(self.game.users_text)

        elif idx == 0:
            self.btn1.setEnabled(False)
            self.player1.setPixmap(QtGui.QPixmap("../_image/player1_move.png"))
            #self.player1_text.append("{}만큼 이동!! 현재 위치는 land[{}]입니다.".format(result, self.game.users[idx].land_idx))

            # 특정 상태를 비교하여 specialplace에 기능 활성화
            if len(self.game.users[idx].countdown2) == 1:
                self.game.game_process2(self.game.users[idx].land_idx, idx)
                # self.game.users[idx].countdown2.clear()

            else:
                ## 땅이 비어있으면 점령, 남에 땅이면 life - 1
                self.game.game_process(self.game.users[idx].land_idx, idx)

            # 빈땅이여서, True 일때만 색을 변경한다.
            if self.game.empty:                    # 해당 유저의 땅 번호, 고유색깔
                self.land_background_color(self.game.users[idx].land_idx, "blue")
            #  QTextBrowser인 main_text player1_text에 데이터 출력
            self.main_text.setPlainText(self.game.main_text)
            self.player1_text.append(self.game.users_text)
            # self.land_text.setPlainText(self.game.total_land)

            self.timer = QTimer(self)
            self.timer.start(1 / 10000)
            self.timer.timeout.connect(self.timeout_run)

        elif idx == 1:
            self.btn1.setEnabled(False)
            self.player2.setPixmap(QtGui.QPixmap("../_image/player2_move.png"))
            #self.player2_text.append("{}만큼 이동!! 현재 위치는 land[{}]입니다.".format(result, self.game.users[idx].land_idx))

            ## 땅이 비어있으면 점령, 남에 땅이면 life - 1
            ## 한번이라도 land_idx == 9 가 나오면 len(countdown2)은 1이 되고 그걸 다시초기화
            if len(self.game.users[idx].countdown2) == 1:
                self.game.game_process2(self.game.users[idx].land_idx, idx)

            else:
                self.game.game_process(self.game.users[idx].land_idx, idx)

            # 빈땅이여서, True 일때만 색을 변경한다.
            if self.game.empty:                    # 해당 유저의 땅 번호, 고유색깔
                self.land_background_color(self.game.users[idx].land_idx, "red")
            #  QTextBrowser인 main_text player2_text에 데이터 출력
            self.main_text.setPlainText(self.game.main_text)
            self.player2_text.append(self.game.users_text)



            # 가상위치 - 이동 이미지 부드럽게 이동 timer
            self.timer = QTimer(self)
            self.timer.start(1 / 10000)
            self.timer.timeout.connect(self.timeout_run)

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
        reAlert = QMessageBox.question(self, '결과', "{0}\n{1}".format(ending_text, last_text), QMessageBox.Yes | QMessageBox.Cancel)

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

    # 스레드 시간단위 실행(이미지 변경)
    def paintEvent(self, e):
        idx = (self.count-1) % self.game.persons
        if idx == 0: self.draw_point(self.player1)
        elif idx == 1: self.draw_point(self.player2)

    # 전달 받은 좌표 값 이미지 표시
    def draw_point(self, qp):
        idx = (self.count-1) % self.game.persons
        qp.setGeometry(self.game.users[idx].virtual.x,
                       self.game.users[idx].virtual.y,
                       self.game.land[idx][self.game.users[idx].land_idx][2],
                       self.game.land[idx][self.game.users[idx].land_idx][3])

    # 스레드 시간단위 실행(기능), virtual_flag: True 실제위치 == 가상위치
    def timeout_run(self):
        idx = (self.count-1) % self.game.persons
        # 실제, 가상위치 비교 및 이동
        virtual_flag, strom_land_idx = self.game.users[idx].virtual_thread(self.game.land[idx])

        # 주사위로 이동한 실제 위치와 이동하는 가상의 위치가 일치할 경우
        # 대기 이미지 변환, 버튼 활성화, 타이머 스탑
        if virtual_flag:
            if idx == 0: self.player1.setPixmap(QtGui.QPixmap("../_image/player1_resize.png"))
            elif idx == 1: self.player2.setPixmap(QtGui.QPixmap("../_image/player2_resize.png"))
            self.btn1.setEnabled(True)
            self.timer.stop()

            if len(self.game.users[idx].countdown2) == 1:
                self.game.users[idx].land_idx = strom_land_idx

            # users의 life가 0이 되었을 때 dice 버튼 비활성화, last_text 출력, QMessageBox 이벤트 발생
            if self.game.users[idx].life == 0:
                last_text = "{}님 땅을 {}개 점령하셨지만 패배하였습니다.. \n 너가 아이스크림 쏘세요".format(self.game.users[idx].name,
                                                                                      self.game.total_land.count(
                                                                                          self.game.users[idx].name))
                self.main_text.setPlainText(last_text)
                self.btn1.setEnabled(False)

                # last_text를 전달해서 창에 띄운다.
                self.result_event(last_text, self.ending_text)
                # QMessageBox.about(self, "결과", self.last_text)

        else:
            self.update()



    #버튼 클릭후 종료
    def rule_close(self):
        self.ruledialog.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainDialog = MainDialog()
    mainDialog.show()
    app.exec_()
