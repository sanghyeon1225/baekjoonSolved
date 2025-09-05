from collections import deque
import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    q = deque([(i, j, data[i][j])])
    visited[i][j] = True
    
    while(q):
        x, y, color = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (n > nx >= 0 and n > ny >= 0 and not visited[nx][ny] and data[nx][ny] == color):
                q.append((nx, ny, color))
                visited[nx][ny] = True

n = int(sys.stdin.readline())
data = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

count = 0
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
            
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if data[i][j] == 'G':
            data[i][j] = 'R'
            
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count2 += 1
            
print(count, count2)