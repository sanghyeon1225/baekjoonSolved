import sys
from collections import deque


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    global data, q
    answer = "IMPOSSIBLE"
    while(q):
        x, y, time = q.popleft()
        if data[x][y] == "J":
            if (x == 0 or x == r-1 or y == 0 or y == c-1):
                return time + 1
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (r > nx >= 0 and c > ny >= 0 and visited[nx][ny] == False and data[nx][ny] == "."):
                    q.append((nx, ny, time + 1))
                    data[nx][ny] = "J"
                    visited[nx][ny] = True
                    
        elif data[x][y] == "F":
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (r > nx >= 0 and c > ny >= 0 and data[nx][ny] not in ("#", "F")):
                    q.append((nx, ny, -1))
                    data[nx][ny] = "F"
    return answer
                
r, c = map(int, sys.stdin.readline().split())

data = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

q = deque([])

for i in range(r):
    for j in range(c):
        if data[i][j] == "J":
            q.append((i, j, 0))
            visited[i][j] = True

for i in range(r):
    for j in range(c):
        if data[i][j] == "F":
            q.append((i, j, -1))

print(bfs())