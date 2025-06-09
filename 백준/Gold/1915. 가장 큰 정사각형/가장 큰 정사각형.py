n, m = map(int, input().split())

data = [list(map(int, input())) for _ in range(n)]


for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and data[i][j] == 1:
            data[i][j] = min(data[i-1][j], data[i][j-1], data[i-1][j-1]) + 1

answer = max(max(row) for row in data) ** 2
print(answer)
    