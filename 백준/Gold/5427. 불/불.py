import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    answer = "IMPOSSIBLE"
    while(q):
        x, y, time = q.popleft()
        if ((x == 0 or x == (r-1) or y == 0 or y == (c-1)) and time > -1):
            answer = time + 1
            return answer
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (r > nx >= 0 and c > ny >= 0 and board[nx][ny] == "."):
                if (time < 0):
                    board[nx][ny] = "*"
                    q.append((nx, ny, -1))
                elif (time > -1 and visited[nx][ny] == False):
                    q.append((nx, ny, time + 1))
                    visited[nx][ny] = True
    return answer

case = int(sys.stdin.readline())

for n in range(case):
    c, r = map(int, sys.stdin.readline().split())

    board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
    
    visited = [[False] * c for _ in range(r)]
    
    q = deque([])

    for i in range(r):
        for j in range(c):
            if board[i][j] == "*":
                q.append((i, j, -1))

    for i in range(r):
        for j in range(c):
            if board[i][j] == "@":
                q.append((i, j, 0))
                visited[i][j] = True
                print(bfs())