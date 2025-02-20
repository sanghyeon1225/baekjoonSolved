from collections import deque
r, c = map(int, input().split())

map = []
for i in range(r):
    map.append(input())

visited = [[False] * c for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(start):
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    while queue:
        count = 0
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if r > nx >= 0 and c > ny >= 0 and map[nx][ny] == '.':
                count += 1
                
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    
        if count < 2:
            return 1
        
    return 0

for i in range(r):
    for j in range(c):
        if map[i][j] == '.':
            start = (i, j)

print(BFS(start))
