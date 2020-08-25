from random import randint


class User:
    def __init__(self, name, life):
        self.name = name
        self.life = life
        self.land_idx = 0

# 주사위 버튼 시 메서드( game 변수목록 클래스, 회차 cnt, 1번째 2번째 유저 구분여부 idx)
    def dice(self, game, count, idx):
# 주사위 돌리기
        result = randint(1, 6)
        print(result)
# 땅 위치 값 계산 후 이동
        self.land_idx += result
# 한바퀴 돌았을 시 idx값 조정
        if self.land_idx > 17:
            self.land_idx -= len(game.land[idx])
# 주사위 값 반환
        return result
'''
    # 주사위 돌리기
    def dice(self, game, count):
        print("{}번째 판입니다!".format(count))
        # 주사위 1개 돌리기
        trigger = input("주사위를 돌리세요 (enter)>>\n")
        result = randint(1, 6)
        print(self.name + "님의 주사위 결과가 {}이(가) 나왔습니다.".format(result))
        # 주사위 나온 값 만큼 이동,
        self.land_idx += result

        # 한바퀴 넘어갈 시 위치 조정
        if self.land_idx >= game.map_size:
            self.land_idx -= game.map_size
            self.life = + 1
            print("한바퀴를 완주하여 목숨이 1개 늘어납니다")

        print("{}칸 이동합니다.".format(result))
        print("{}님의 현재 위치는 {}입니다.".format(self.name, self.land_idx))

        # 땅 이동시에 해당 땅일시 결과
        # 미소유 땅 = 점령, 상대방 점령된 땅 = 목숨 잃음, 내가 점령한 땅 = 그대로
        if game.land[self.land_idx] == "":
            game.land[self.land_idx] = self.name
            print("{0}번 땅을 {1}님이 점령했습니다.".format(self.land_idx, self.name))
        # 상대방 점령된 땅 = 목숨 잃음
        elif game.land[self.land_idx] != self.name:
            self.life -= 1
            print("{0}님의 땅을 밟아 {1}님이 목숨을 1개 잃었습니다.".format(game.land[self.land_idx], self.name))
            print("{0}님의 남은 목숨의 개수는 {1}개 입니다.".format(self.name, self.life))
            # 목숨을 잃고, life 0이 되면 게임 종료
            if self.life == 0:
                return True
        elif game.land[self.land_idx] == self.name:
            print("{0}님이 자신의 땅을 밟아 목숨이 유지됩니다.".format(self.name))

        print("\n")
        return False
'''


