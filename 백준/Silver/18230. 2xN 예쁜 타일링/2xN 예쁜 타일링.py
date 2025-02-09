n = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
answer = 0
count = 0
if n[0] % 2 == 1:
    answer += a[-1]
    a.pop(-1)
    n[0] -= 1

for i in range(0, n[0], 2):
    x1, x2 = 0, 0
    if len(a) >= 2:
        x1 = a[-1] + a[-2]
    if len(b) >= 1:
        x2 = b[-1]
    
    if x1 > x2:
        answer += x1
        a.pop()
        a.pop()
    else:
        answer += x2
        b.pop()
print(answer)
