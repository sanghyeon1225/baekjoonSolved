import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
    

def bfs():
    global data, r, c
    
    q = deque([])
    for i in range(r):
        for j in range(c):
            if data[i][j] == 1:
                q.append((i, j))
    
    while(q):
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if (r > nx >= 0 and c > ny >= 0 and data[nx][ny] == 0):
                data[nx][ny] = data[x][y] + 1
                q.append((nx, ny))
                
            
c, r = map(int, sys.stdin.readline().split())

data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(r)]

bfs()

answer = 0
flag = False

for i in range(r):
    for j in range(c):
        if data[i][j] == 0:
            flag = True            
        answer = max(answer, data[i][j])

if flag:
    print(-1)
else:
    print(answer - 1)

