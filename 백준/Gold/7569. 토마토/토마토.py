from collections import deque

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    global answer
    while(q):
        x, y, z, time = q.popleft()
        answer = time
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if (n > nx >= 0 and m > ny >= 0 and h > nz >= 0 and not visited[nz][nx][ny] and data[nz][nx][ny] == 0):
                q.append((nx, ny, nz, time + 1))
                visited[nz][nx][ny] = True
                data[nz][nx][ny] = 1
    
m, n, h = map(int, input().split())

data = []

for i in range(h):
    data1 = []    
    for j in range(n):
        data1.append(list(map(int, input().split())))
    data.append(data1)

visited = [[[False] * m for _ in range(n)] for _ in range(h)]

q = deque([])

answer = -1

for k in range(h):
    for i in range(n):
        for j in range(m):
            if data[k][i][j] == 1:
                q.append((i, j, k, 0))
                visited[k][i][j] = True
bfs()

flag = True

for k in range(h):
    for i in range(n):
        for j in range(m):
            if data[k][i][j] == 0:
                flag = False
if flag:
    print(answer)
else:
    print(-1)