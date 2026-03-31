import sys

n = int(sys.stdin.readline().rstrip())

data = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

dp = [0] * n

if n == 1:
    print(data[0])
elif n == 2:
    print(data[0] + data[1])
else:
    dp[0] = data[0]
    dp[1] = data[0] + data[1]
    dp[2] = max(dp[1], data[0] + data[2], data[1] + data[2])

    for i in range(3, n):
        # 1. 이번 잔을 안 마시는 경우 (이전까지의 최댓값 유지)
        # 2. 이번 잔이 1연속인 경우 (전 잔은 안 마심)
        # 3. 이번 잔이 2연속인 경우 (전 잔은 마시고, 전전 잔은 안 마심)
        dp[i] = max(dp[i-1], data[i] + dp[i-2], data[i] + data[i-1] + dp[i-3])

    print(max(dp))