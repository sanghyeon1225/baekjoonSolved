r, c = map(int, input().split())
map = [['.'] * c for i in range(r)]
map2 = [['.'] * c for i in range(r)]

for i in range(r):
    j = 0
    for _ in input():
        if _ == 'X':
            map[i][j] = 'X'
        j += 1

for i in range(r):
    for j in range(c):
        map2[i][j] = map[i][j] # 원본 map을 map1에 복사

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(r):
    for j in range(c):
        sea = 0
        if map[i][j] == 'X':
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    sea += 1
                elif map[nx][ny] == '.':
                    sea += 1
            
            if sea > 2:
                map2[i][j] = '.'

row = []
col = []

for i in range(r):
    for j in range(c):
        if map2[i][j] == 'X':
            row.append(i)
            col.append(j)

if (row):
    min_row = min(row)
    max_row = max(row)
    min_col = min(col)
    max_col = max(col)

    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            print(map2[i][j], end="")
        print()
else:
    print('X')