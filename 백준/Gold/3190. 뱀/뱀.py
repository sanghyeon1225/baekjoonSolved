import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

board = [[0] * N for _ in range(N)]

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = -1

L = int(sys.stdin.readline().rstrip())

directions = deque([])

for _ in range(L):
    time, c = sys.stdin.readline().split()
    directions.append((int(time), c))

snake = deque([])
snake.append((0, 0))

dx = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽, 위
dy = [1, 0, -1, 0]

answer = 0
now_d = 0

for i in range(999999):
    now_x, now_y = snake[-1]
    
    # 방향 전환 로직
    if (directions and directions[0][0] == answer):
        t, d = directions.popleft()
        if d == 'D':
            now_d = (now_d + 1) % 4
        else:
            if now_d == 0:
                now_d = 3
            else:
                now_d -= 1
    
    # 다음 좌표 연산 및 정상일 시 이동
    nx, ny = now_x + dx[now_d], now_y + dy[now_d]
    
    if (N > nx >= 0 and N > ny >= 0 and (nx, ny) not in snake):
        snake.append((nx, ny))
    else:
        break
    
    #사과를 안만났다면 뱀 꼬리 제거
    if board[nx][ny] != -1 :
        snake.popleft()
    else:
        board[nx][ny] = 0
    
    answer += 1

print(answer + 1)
