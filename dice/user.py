from random import randint
from dice.virtual import Virtual


class User:
    def __init__(self, name, life, x, y):
        self.name = name
        self.life = life
        self.land_idx = 0
        self.virtual = Virtual(x, y)
        self.result = 0
        self.circle_text = ""
        # 무인도 변수
        self.countdown = []
        # 폭풍 변수
        self.countdown2 = []

    # 실제위치 메서드( game 변수목록 클래스, 회차 cnt, 1번째 2번째 유저 구분여부 idx) - 실제 위치
    # 주사위 돌리기, 땅 위치 값 계산 후 이동, 한바퀴 돌았을 시 idx값 조정, 주사위 값 반환
    def dice(self, game, count, idx):
        # 주사위 돌리기
        self.result = randint(1, 6)
        # 땅 위치 값 계산 후 이동
        self.land_idx += self.result
        # 한바퀴 돌았을 시 idx값 조정, life +1
        if self.land_idx > 17:
            self.land_idx -= len(game.land[idx])
            self.life += 1
            self.circle_text = "한바퀴가 지났습니다. 생명력 +1 !!"
        # 한바퀴 돌고 두번째 이후  text를 비운다.
        else:
            self.circle_text = ""
        # 주사위 값 반환, 객체 변수로 만들어서 Game 클래스에서 주사위 값 사용
        return self.result

    # 실제, 가상위치 비교 및 이동
    def virtual_thread(self, land):
        # 실제, 가상위치 일치
        if self.land_idx == self.virtual.idx:
            return True, randint(1, 17)
        # 실제, 가상위치 불일치
        else:
            self.virtual.move_run(land)
            return False, 0


