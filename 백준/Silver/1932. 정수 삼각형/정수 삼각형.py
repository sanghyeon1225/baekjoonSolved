import sys
n = int(sys.stdin.readline().rstrip())
dp = [[0] * n for _ in range(n+1)]
dp[1][0] = int(sys.stdin.readline())

for i in range(2, n + 1):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(i):
        if j == 0:
            dp[i][j] = data[j] + dp[i-1][j]
        elif j == (i-1):
            dp[i][j] = data[j] + dp[i-1][j-1]
        else:
            dp[i][j] = data[j] + max(dp[i-1][j-1], dp[i-1][j])
    
print(max(dp[-1]))
            