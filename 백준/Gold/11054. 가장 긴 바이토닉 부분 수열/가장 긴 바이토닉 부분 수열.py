n = int(input())

data = list(map(int, input().split()))
increase = [1] * n
decrease = [1] * n

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            increase[i] = max(increase[i], increase[j] + 1)


for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if data[i] > data[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
            
result = 0
for i in range(n):
    result = max(result, increase[i] + decrease[i] - 1)

print(result)