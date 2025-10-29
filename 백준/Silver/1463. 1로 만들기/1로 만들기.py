n = int(input())

count = 0
D = [0] * 1000001

for i in range(2, 1000001):
    D[i] = D[i-1] + 1
    if (i % 2 == 0):
        D[i] = min(D[i], D[i // 2] + 1)
    if (i % 3 == 0):
        D[i] = min(D[i], D[i // 3] + 1) 

print(D[n])