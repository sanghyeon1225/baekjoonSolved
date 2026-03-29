import sys

n = int(sys.stdin.readline().rstrip())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]

for i in range(3):
    dp[0][i] = data[0][i]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + data[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + data[i][j]
        else:
            dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + data[i][j]

print(min(dp[n-1]))