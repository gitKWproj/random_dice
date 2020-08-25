from mymodify.dice.user import User
from random import randint


class Game:
    def __init__(self):
        self.persons = 2
        self.start_life = 0
        self.map_size = 18
        # self.users 에 User 객체가 들어가 있다.
        self.users = []
        self.land = []
        for i in range(self.map_size):
            self.land.append("")
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

    # 선공 정하기 함수
    def toss_coin(self):
        result = randint(0, 1)
        return result

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

    def start(self):
        print("랜덤 다이스에 오신것을 환영합니다~!. 게임을 시작하겠습니다.")

        # input(persons map_size start_life)
        # ex) 2 17 3
        input_result = input("인원 수, 목숨을 입력해주세요\nex)2 3\n")
        input_list = input_result.split(" ")

        # Game(persons, start_life)
        self.persons = int(input_list[0])
        self.start_life = int(input_list[1])

        self.input_name()

    def input_name(self, user_name1, user_name2):
        # User 닉네임 입력
        self.users.append(User(user_name1, self.start_life))
        self.users.append(User(user_name2, self.start_life))
