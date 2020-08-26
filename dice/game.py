from dice.user import User
from random import randint


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
        self.users.append(User(user_name1, self.start_life))
        self.users.append(User(user_name2, self.start_life))
        self.users.append([user_name1, user_name2])

    # 빈땅이면 점령 자기땅이면 pass 상대방 땅이면 life - 1
    def game_process(self, land_idx, idx):

        if self.total_land[land_idx] == "":
            self.total_land[land_idx] = self.users[2][idx]

        elif self.total_land[land_idx] == self.users[2][idx]:
            print("본인 땅입니다.")
        elif self.total_land[land_idx] != self.users[2][idx]:
            self.users[idx].life -= 1
            print(self.users[idx].life)


    def game_over(self):
        temp_list = []
        land_set = set(self.land)

        print("\n")

        for i in land_set:
            temp_list.append([i, self.land.count(i)])

        for i in range(len(temp_list)):
            if temp_list[i][0] == "":
                print("미점령된 땅의 개수 - {0}".format(temp_list[i][1]))
            else:
                print("{0}님의 땅의 개수 - {1}".format(temp_list[i][0], temp_list[i][1]))

        # 변수에 승자 땅 갯수, 승자명 담기
        land_count = 0
        winner = ""
        for i in land_set:
            if i == "": continue

            # 처음일 때,
            if land_count == 0:
                winner = i
                land_count = self.land.count(i)
                continue

            # 땅의 갯수가 같을때
            if land_count == self.land.count(i):
                winner = winner + ",{}".format(i)
            # 땅의 갯수가 더 많을때
            elif land_count < self.land.count(i):
                winner = i
                land_count = self.land.count(i)

        # 비겼을 때
        if winner.find(",") != -1:
            print("\n비겼습니다!\n")
            return
        # 결과가 나왔을 때
        print("\n{0}님이 승리하셨습니다!\n".format(winner))

