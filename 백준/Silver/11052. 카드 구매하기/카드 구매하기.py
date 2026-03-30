import sys
n = int(input())
data = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(i + 1):
        dp[i] = max(dp[i], dp[i - j] + data[j])

print(dp[n])