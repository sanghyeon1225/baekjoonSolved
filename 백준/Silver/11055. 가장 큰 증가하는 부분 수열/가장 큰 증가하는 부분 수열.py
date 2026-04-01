n = int(input())

data = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = data[i]
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + data[i])

print(max(dp))