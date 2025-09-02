import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
    
def bfs(i, j):
    q = deque([(i, j, 1)])
    visited[i][j] = True
    
    while(q):
        x, y, count = q.popleft()
        
        if x == r-1 and y == c-1:
            return count
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if (r > nx >= 0 and c > ny >= 0 and not visited[nx][ny] and data[nx][ny]):
                visited[nx][ny] = True
                q.append((nx, ny, count + 1))

r, c = map(int, sys.stdin.readline().split())

data = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(r)]

visited = [[False] * c for _ in range(r)]

print(bfs(0, 0))