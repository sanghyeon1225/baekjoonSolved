import sys

n = int(sys.stdin.readline())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(len(data) - 2, -1, -1):
    for j in range(len(data[i])):
        data[i][j] = max(data[i][j] + data[i+1][j], data[i][j] + data[i+1][j+1])

print(data[0][0])