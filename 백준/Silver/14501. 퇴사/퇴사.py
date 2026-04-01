n = int(input())

time = [0]
value = [0]

dp = [0] * (n+2)

for i in range(n):
    t, v = map(int, input().split())
    time.append(t)
    value.append(v)
    
for i in range(n, 0, -1):
    t = time[i]
    v = value[i]
    
    if i + t <= n + 1: 
        dp[i] = max(v + dp[i + t], dp[i + 1])
    else: 
        dp[i] = dp[i + 1]

print(max(dp))