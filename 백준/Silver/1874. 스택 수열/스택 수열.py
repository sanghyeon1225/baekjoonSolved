n = int(input())

data = [int(input()) for _ in range(n)]

answer = []

stack = [0]

now = 0

for i in range(n):
    while (stack[-1] < data[i]):
        now += 1
        answer.append("+")
        stack.append(now)
    if stack[-1] == data[i]:
        answer.append("-")
        stack.pop()
    else:
        print("NO")
        exit() 

for i in range(len(answer)):
    print(answer[i])
