n = int(input())
data = list(map(int, input().split()))

right = [-1] * n
stack = []
for i in range(n - 1, -1, -1):
    while(len(stack) != 0 and stack[-1] <= data[i]):
        stack.pop()
    if (len(stack) != 0):
        right[i] = stack[-1]
    else:
        right[i] = -1
    stack.append(data[i])

for i in range(n):
    if (i != n-1):
        print(right[i], end = " ")
    else:
        print(right[i])