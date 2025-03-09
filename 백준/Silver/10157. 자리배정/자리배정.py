import sys

c, r = map(int, sys.stdin.readline().split())
target = int(sys.stdin.readline())

x = r-1
y = 0

if target > c * r:
    print(0)
    sys.exit()
    
visited = [[False]*c for i in range(r)] 

dx = [-1, 0, 1, 0] # 상, 우, 하, 좌
dy = [0, 1, 0, -1]

count = 1
direction = 0
visited[x][y] = True
    
while(count < target):
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if not (r > nx >= 0 and c > ny >= 0) or visited[nx][ny]:
        direction = (direction + 1) % 4
        nx = x + dx[direction]
        ny = y + dy[direction]
        
    x, y = nx, ny
    visited[x][y] = True
    count += 1
    
print(y+1, r-x)