n, x = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

weight = 0
flag = True


for i in range(n):
    weight += b[i]
    
    if weight < a[i]:
        flag = False
        break


if flag:
    print(int((weight - a[n-1]) / x))
else:
    print(-1)