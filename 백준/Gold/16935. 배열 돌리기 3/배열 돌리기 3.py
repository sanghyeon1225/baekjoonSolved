
def op1(data):
    return data[::-1]

def op2(data):
    return [row[::-1] for row in data]

def op3(data, n, m):
    new_data = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_data[j][n-1-i] = data[i][j]
    return new_data

def op4(data, n, m):
    new_data = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_data[m-1-j][i] = data[i][j]
    return new_data

def op5(data, n, m):
    new_data = [[0] * m for _ in range(n)]
    nn, mm = n // 2, m // 2
    for i in range(nn):
        for j in range(mm):
            new_data[i][j+mm] = data[i][j]
            new_data[i+nn][j+mm] = data[i][j+mm]
            new_data[i+nn][j] = data[i+nn][j+mm]
            new_data[i][j] = data[i+nn][j]
    return new_data

def op6(data, n, m):
    new_data = [[0] * m for _ in range(n)]
    nn, mm = n // 2, m // 2
    for i in range(nn):
        for j in range(mm):
            new_data[i][j+mm] = data[i+nn][j+mm]
            new_data[i+nn][j+mm] = data[i+nn][j]
            new_data[i+nn][j] = data[i][j]
            new_data[i][j] = data[i][j+mm]
    return new_data

n, m, r = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

cmds = list(map(int, input().split()))

for cmd in cmds:
    if cmd == 1:
        data = op1(data)
    elif cmd == 2:
        data = op2(data)
    elif cmd == 3:
        data = op3(data, n, m)
        n, m = m, n
    elif cmd == 4:
        data = op4(data, n, m)
        n, m = m, n
    elif cmd == 5:
        data = op5(data, n, m)
    elif cmd == 6:
        data = op6(data, n, m)

for row in data:
    print(*row)