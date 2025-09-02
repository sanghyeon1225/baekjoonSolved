import sys
from collections import deque

def bfs(i, j):
    count = 1
    q = deque([[i, j]])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[i][j] = True
    while(q):
        now = q.popleft()
        x, y = now[0], now[1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (r > nx >= 0 and c > ny >= 0):
                if (not visited[nx][ny] and data[nx][ny]):
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    count += 1
    return count        

r, c = map(int, sys.stdin.readline().split())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

visited = [[False] * c for _ in range(r)]

bfs_count = 0
answer = 0

for i in range(r):
    for j in range(c):
        if (data[i][j] and not visited[i][j]):
            bfs_count += 1
            answer = max(answer, bfs(i, j))

print(bfs_count)
print(answer)