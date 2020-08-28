from random import randint
from mymodify.dice.virtual import Virtual


class User:
    def __init__(self, name, life, x, y):
        self.name = name
        self.life = life
        self.land_idx = 0
        self.virtual = Virtual(x, y)

    # 실제위치 메서드( game 변수목록 클래스, 회차 cnt, 1번째 2번째 유저 구분여부 idx) - 실제 위치
    # 주사위 돌리기, 땅 위치 값 계산 후 이동, 한바퀴 돌았을 시 idx값 조정, 주사위 값 반환
    def dice(self, game, count, idx):
        result = randint(1, 6)
        self.virtual.idx = self.land_idx
        self.land_idx += result

        if self.land_idx > 17:
            self.land_idx -= len(game.land[idx])
        return result

    # 실제, 가상위치 비교 및 이동
    def virtual_thread(self, land):
        # 실제, 가상위치 일치
        if self.land_idx == self.virtual.idx:
            return True
        # 실제, 가상위치 불일치
        else:
            self.virtual.move_run(land)
            return False


