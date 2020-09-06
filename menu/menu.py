from dice.game import Game


class Menu:
    def __init__(self, page_number):
        self.now_page = page_number

    def page1(self):
        # 게임 시작, 1페이지 저장
        self.now_page = 1
        new_game = Game()

        # 동전 던지기 구현(일단 패스) - 선공, 후공 순서 정하기


        # 입력 값 전부 입력, 게임 시작
        # count - 현재 돌아가는 판 몇번째인지 카운트 , flag - False 게임진행, True - 게임종료
        count = 0
        flag = False
        while True:
            print("현재 땅 상태 - {}".format(new_game.land))
            idx = count % new_game.persons

            count = count + 1

            # new_game에 리스트형태로 보관중인 현재 플레이중인 유저 값 가져오기
            now_play_user = new_game.users[idx]
            flag = now_play_user.dice(new_game, count)

            # 누군가가 목숨이 다 했을경우 게임종료
            if flag is True:
                new_game.game_over()
                break

    def page2(self):
        self.now_page = 2
        print("게임을 불러옵니다.")
