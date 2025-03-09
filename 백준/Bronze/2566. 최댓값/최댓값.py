n = 9
data = [list(map(int, input().split())) for _ in range(n)]

max_num = 0
max_x, max_y = 0, 0
for i in range(n):
    for j in range(n):
        if data[i][j] >= max_num:
            max_num = data[i][j]
            max_x, max_y = i, j
print(max_num)
print(max_x+1, max_y+1)