import sys
from collections import deque

dx = [-1, -1, -2, -2, 1, 1, 2, 2]
dy = [-2, 2, -1, 1, -2, 2, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while(q):
        now_x, now_y = q.popleft()
        
        if (now_x == target_x and now_y == target_y):
            return board[now_x][now_y]
        
        for i in range(8):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if (n > nx >= 0 and n > ny >= 0 and not visited[nx][ny]):
                q.append((nx, ny))
                visited[nx][ny] = True
                board[nx][ny] = board[now_x][now_y] + 1
        

case_number = int(sys.stdin.readline())

for i in range(case_number):
    n = int(sys.stdin.readline())
    x, y = map(int, sys.stdin.readline().split())
    target_x, target_y = map(int, sys.stdin.readline().split())
    
    board = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    print(bfs(x, y))
    