n = int(input())

data = list(map(int, input().split()))

dp = [[x] for x in data]

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            if len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [data[i]]
answer_list = max(dp, key=len)
print(len(answer_list))
print(*answer_list)