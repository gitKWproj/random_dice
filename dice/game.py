from dice.user import User


class Game:
    def __init__(self):
        self.persons = 2
        self.start_life = 0
        self.map_size = 18
        # self.users 에 User 객체가 들어가 있다.
        self.users = []
        self.total_land = []
        for i in range(self.map_size):
            self.total_land.append("")
        self.main_text = ""
        self.users_text = ""
        self.last_test = ""
        # 본인 땅과 남의 땅을 구별해주는 변수 empty
        self.empty = False
        #users[0] 과 users[1] 의 이미지 위치값
        self.land = [
            [(610, 470, 40, 40), (510, 470, 40, 40), (410, 470, 40, 40), (310, 470, 40, 40), (210, 470, 40, 40),
            (110, 470, 40, 40),
            (110, 370, 40, 40), (110, 270, 40, 40), (110, 170, 40, 40), (110, 70, 40, 40),
            (210, 70, 40, 40), (310, 70, 40, 40), (410, 70, 40, 40), (510, 70, 40, 40), (610, 70, 40, 40),
            (610, 170, 40, 40), (610, 270, 40, 40), (610, 370, 40, 40)],

            [(650, 510, 40, 40), (550, 510, 40, 40), (450, 510, 40, 40), (350, 510, 40, 40), (250, 510, 40, 40),
            (150, 510, 40, 40),
            (150, 410, 40, 40), (150, 310, 40, 40), (150, 210, 40, 40), (150, 110, 40, 40),
            (250, 110, 40, 40), (350, 110, 40, 40), (450, 110, 40, 40), (550, 110, 40, 40), (650, 110, 40, 40),
            (650, 210, 40, 40), (650, 310, 40, 40), (650, 410, 40, 40)]
        ]

    def input_name(self, user_name1, user_name2):
        # User 닉네임 입력
        self.users.append(User(user_name1, self.start_life, self.land[0][0][0], self.land[0][0][1]))
        self.users.append(User(user_name2, self.start_life, self.land[1][0][0], self.land[1][0][1]))
        self.users.append([user_name1, user_name2])

    # 빈땅이면 점령 자기땅이면 pass 상대방 땅이면 life - 1
    def game_process(self, land_idx, idx):
        # main_text와 users_text 데이터 설정, 빈 땅일때, land_idx 가 0이 아닐때만

        if land_idx == 5:
            self.empty = False
            self.users[idx].countdown.append("무인도")
            self.users_text = """
        무인도에 도착했습니다
        3턴동안 움직일수 없습니다
        """
        # 폭풍 추가
        elif land_idx == 9:
            self.empty = False
            self.main_text = "폭풍의 지역입니다."
            self.users_text = """
        폭풍을 만났습니다
        어디론가 날아갑니다
        (다음턴에 임의에 land로 이동합니다)
        """
 #           self.users[idx].land_idx = randint(1, 17)
            self.users[idx].countdown2.append("조난중")


        # 아무도 소유하지 않을 땅일때
        elif self.total_land[land_idx] == "" and land_idx != 0:
            # 빈땅이면 True
            self.empty = True
            self.total_land[land_idx] = self.users[2][idx]
            self.main_text = "{}의 주사위 {} !!!".format(self.users[2][idx], self.users[idx].result)
            self.users_text = "{}만큼 이동!! 현재 위치는 land[{}]입니다. \n{} 남은 생명력 {}".format(
                self.users[idx].result, self.users[idx].land_idx, self.users[idx].circle_text, self.users[idx].life)
        # 자기 땅일 때
        elif self.total_land[land_idx] == self.users[2][idx] and land_idx != 0:
            self.main_text = "{}의 주사위 {} !!!".format(self.users[2][idx], self.users[idx].result)
            self.users_text = "{}만큼 이동!! 현재 위치는 land[{}] 본인 땅입니다. \n{} 남은 생명력 {}".format(
                self.users[idx].result, self.users[idx].land_idx, self.users[idx].circle_text, self.users[idx].life)
        # 남의 땅일 때
        elif self.total_land[land_idx] != self.users[2][idx] and land_idx != 0:
            # 남의 땅이면 False
            self.empty = False
            self.users[idx].life -= 1
            self.main_text = "{}의 주사위 {} !!!".format(self.users[2][idx], self.users[idx].result)
            self.users_text = "{}만큼 이동!! 현재 위치는 land[{}] 상대방의 땅입니다. 생명력 -1\n{} 남은 생명력 {}".format(
                self.users[idx].result, self.users[idx].land_idx, self.users[idx].circle_text, self.users[idx].life)
        # 시작 지점일 때
        elif land_idx == 0:
            self.main_text = "{}의 주사위 {} !!!".format(self.users[2][idx], self.users[idx].result)
            self.users_text =  "{}만큼 이동!! 현재 위치는 land[{}] 시작지점입니다. \n생명력 +1 남은 생명력 {}".format(
                self.users[idx].result, self.users[idx].land_idx, self.users[idx].life)

        # 폭풍으로 이동후 상황에 맞는 player_text를 반환 하기 위한 함수 및 이동후에 같은 기능 활성화
        # land_idx == 9 일 때, 단 한번 실행함
    def game_process2(self, land_idx, idx):
        # 이 함수를 실행시키면 countdown2 리스트를 비운다.
        self.users[idx].countdown2.clear()
        self.main_text = "임의 장소로 이동중..."
        if land_idx == 5:
            self.empty = False
            self.users[idx].countdown.append("무인도")
            self.users_text = """눈을 떠보니
        무인도에 도착했습니다
        3턴동안 움직일수 없습니다
        """

        elif land_idx == 9:
            self.empty = False
            self.users_text = """ 
        다시한번 폭풍을 만났습니다
        어디론가 날아갑니다
        (다음턴에 임의에 land로 이동합니다)
        """
#            self.users[idx].land_idx = randint(1, 17)
            self.users[idx].countdown2.append("조난중")

        elif self.total_land[land_idx] == "" and land_idx != 0:
            # 빈땅이면 True
            self.empty = True
            # 현재땅의 위치에  유저 name 값을 구분하여 삽입
            self.total_land[land_idx] = self.users[2][idx]
            self.users_text = "눈을떠보니 현재 위치는 land[{}]입니다. \n{} 남은 생명력 {}".format(
                self.users[idx].land_idx, self.users[idx].circle_text, self.users[idx].life)
            # 자기 땅일 때
        elif self.total_land[land_idx] == self.users[2][idx] and land_idx != 0:
            self.users_text = "눈을떠보니 현재 위치는 land[{}] 본인 땅입니다. \n{} 남은 생명력 {}".format(
                self.users[idx].land_idx, self.users[idx].circle_text, self.users[idx].life)
            # 남의 땅일 때
        elif self.total_land[land_idx] != self.users[2][idx] and land_idx != 0:
            # 남의 땅이면 False
            self.empty = False
            self.users[idx].life -= 1
            self.users_text = "눈을떠보니 현재 위치는 land[{}] 상대방의 땅입니다. \n{} 남은 생명력 {}".format(
                self.users[idx].land_idx, self.users[idx].circle_text, self.users[idx].life)
            # 시작 지점일 때
        elif land_idx == 0:
            self.users_text = "눈을떠보니 현재 위치는 land[{}] 시작지점입니다. \n생명력 +1 남은 생명력 {}".format(
                self.users[idx].land_idx, self.users[idx].life)

            # 무인도 실행

    def specialplace1(self, idx):
        self.users[idx].countdown.append("무인도")
        if len(self.users[idx].countdown) == 2:
            self.users_text = """
        2턴 남았습니다
        """

        if len(self.users[idx].countdown) == 3:
            self.users_text = """
        1턴 남았습니다
        """
        if len(self.users[idx].countdown) == 4:
            self.users_text = """
        돛단배 완성!
        돛단배를 타고 탈출합니다
        다음턴부터 이동하세요
        """
            self.users[idx].land_idx = 5
            self.users[idx].countdown.clear()


