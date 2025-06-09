from collections import deque

def bfs(i, j):
    global visited
    global data
    global count 
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[i][j] = 1
    q = deque([[i, j]])
    
    while(q):
        next = q.popleft()
        for i in range(4):
            nx = next[0] + dx[i]
            ny = next[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1
    count += 1
        

n = int(input())

for i in range(n):
    m, n, k = map(int, input().split())
    count = 0
    
    data = [[0] * m for _ in range(n)]
    
    visited = [[0] * m for _ in range(n)]
    
    for i in range(k):
        x, y = map(int, input().split())
        data[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if(data[i][j] == 1 and visited[i][j] == 0):
                bfs(i, j)
    
    print(count)
    