# 브루트 포스로 벽 세우기
# 세울 때 마다 bfs 돌려서 안전 구역 구하고 최대값만 저장하기
from itertools import combinations
from collections import deque

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

# 0 빈칸, 1 벽, 2 바이러스
empty = []
virus = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
max_count = 0

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            empty.append((i, j))
        elif data[i][j] == 2:
            virus.append((i, j))

for now in combinations(empty, 3):
    new_data = [row[:] for row in data]
    for com_x, com_y in now:
        new_data[com_x][com_y] = 1
        
    deq = deque(virus)
    
    while(deq):
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (n > nx >= 0 and m > ny >= 0 and new_data[nx][ny] == 0):
                new_data[nx][ny] = 2
                deq.append((nx, ny))
    count = 0
    for r in new_data:
        count += r.count(0)
    
    max_count = max(max_count, count)

print(max_count)