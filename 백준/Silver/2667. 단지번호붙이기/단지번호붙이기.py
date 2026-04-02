from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    count = 1
    q = deque([(i, j)])
    
    visited[i][j] = True
    while(q):
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (n > nx >= 0 and len(graph[0]) > ny >= 0 and graph[nx][ny] == 1 and visited[nx][ny] == False):
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1
    return count
    
n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

visited = [[False] * len(graph[0]) for _ in range(n)]

answer = []

for i in range(n):
    for j in range(len(graph[0])):
        if graph[i][j] == 1 and visited[i][j] == False:
            bfs_count = bfs(i, j)
            answer.append(bfs_count)

answer.sort()

print(len(answer))      
for ans in answer:
    print(ans)
    