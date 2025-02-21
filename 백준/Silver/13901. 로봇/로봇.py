r, c = map(int, input().split())

room = [[0] * c for _ in range(r)]

object = int(input())
obPos = []
for i in range(object):
    x, y = map(int, input().split())
    obPos.append((x, y))

startX, startY = map(int, input().split())

direction = list(map(int, input().split()))

for i, j in obPos:
    room[i][j] = 'x'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x = startX
y = startY
idx = 0
flag = True
blockCount = 0
while(flag):
    nx = x + dx[direction[idx % len(direction)] - 1]
    ny = y + dy[direction[idx % len(direction)] - 1]
    
    if (r > nx >= 0 and c > ny >= 0 and room[nx][ny] == 0):
        room[x][y] = 1
        x = nx
        y = ny
        blockCount = 0
    else:
        if blockCount == len(direction):
            flag = False
            print(x, y)
        blockCount += 1
        idx += 1