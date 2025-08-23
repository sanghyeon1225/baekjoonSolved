number, n = map(int, input().split())

data = []

for i in range(1, number + 1):
    if (number % i == 0):
        data.append(i)
    if (len(data) == n):
        break
if (len(data) < n):
    print(0)
else:
    print(data[n-1])