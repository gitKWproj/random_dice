class Virtual:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.idx = 0

    # 주사위로 이동한 실제 위치와 이동하는 가상의 위치가 불일치할 경우
    # 가상의 위치와 가상의 위치 +1의 위치를 비교하여 추가되는 위치값의 좌표(x or y)를 + 1 만큼 이동
    # 좌표 0 <= idx < 5 -> 서쪽 이동,
    # 좌표 5 <= idx <= 9 -> 북쪽 이동,
    # 좌표 9 <= idx <= 14 -> 동쪽 이동,
    # 좌표 14 <= idx <= 17 -> 남쪽 이동,
    # 좌표 17 -> 남쪽 이동이지만 다음 위치값 참조가 첫번째 땅 값이므로 별도로 생성
    def move_run(self, land):
        if self.idx < 5:
            self.x -= 1
            if land[self.idx+1][0] == self.x:
                self.idx += 1
        elif 5 <= self.idx & self.idx < 9:
            self.y -= 1
            if land[self.idx+1][1] == self.y:
                self.idx += 1
        elif 9 <= self.idx & self.idx < 14:
            self.x += 1
            if land[self.idx+1][0] == self.x:
                self.idx += 1
        elif 14 <= self.idx & self.idx < 17:
            self.y += 1
            if land[self.idx+1][1] == self.y:
                self.idx += 1
        elif self.idx == 17:
            self.y += 1
            if land[0][1] == self.y:
                self.idx = 0
        return False




