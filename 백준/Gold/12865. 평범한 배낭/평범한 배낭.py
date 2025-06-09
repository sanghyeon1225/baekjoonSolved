n, k = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

data.insert(0, [0,0])

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = data[i][0]
        value = data[i][1]
        
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])
            
print(dp[n][k])