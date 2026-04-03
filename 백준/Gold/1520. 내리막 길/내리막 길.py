import sys

sys.setrecursionlimit(10**6)

def dfs(i, j):
    if i == (m-1) and j == (n-1):
        return 1
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    dp[i][j] = 0
    
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if (m > nx >= 0 and n > ny >= 0 and data[i][j] > data[nx][ny]):
            dp[i][j] += dfs(nx, ny)
    
    return dp[i][j]

m, n = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

answer = dfs(0, 0)

print(answer)