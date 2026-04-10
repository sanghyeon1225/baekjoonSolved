import sys

n, m = map(int, sys.stdin.readline().split())

x, y, direct = map(int, sys.stdin.readline().split())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

clean = 0
# 0이 빈칸, 1이 벽, 2가 청소된 공간
while True:
    # 청소
    if data[x][y] == 0:
        data[x][y] = 2
        clean += 1
        
    count = 0
    # 주변 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 주변 청소할 곳이 있는지 확인
        if (n > nx >= 0 and m > ny >= 0 and data[nx][ny] == 0):
            count += 1
        
    if (count != 0):
        # 방향 전환 90도 -> 1번으로 돌아가기
        if direct == 0:
            direct = 3
        else:
            direct -= 1
        
        nx, ny = x + dx[direct], y + dy[direct]
        if (n > nx >= 0 and m > ny >= 0 and data[nx][ny] == 0):
            x, y = nx, ny
        
    # 주변 청소할 곳이 없다면 후진
    if count == 0:
        # 후진
        back_x, back_y = x + dx[(direct + 2) % 4], y + dy[(direct + 2) % 4]
        # 정상 범주라면 좌표 수정
        if (n > back_x >= 0 and m > back_y >= 0 and data[back_x][back_y] != 1):
            x, y = back_x, back_y
        else:   
            print(clean)
            exit()
    