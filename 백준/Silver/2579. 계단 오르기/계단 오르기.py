import sys

n = int(sys.stdin.readline())

data = [0] + [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * (n + 1)
if n >= 1:
    dp[1] = data[1]
if n >= 2:
    dp[2] = data[1] + data[2]
if n >= 3:
    dp[3] = max(data[1] + data[3], data[2] + data[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + data[i-1] + data[i], dp[i-2] + data[i])
    
print(dp[n])