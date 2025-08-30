n = int(input())

for i in range(n):
    n0, n1 = 1, 0
    target = int(input())
    for j in range(target):
        n0, n1 = n1, (n0 + n1)
    print(n0, n1)
    
