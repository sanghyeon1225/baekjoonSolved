from collections import deque

n, m = map(int, input().split())

data = deque([i+1 for i in range(n)])

target = list(map(int, input().split()))

count = 0

for i in range(m):
    while(1):
        if target[i] == data[0]:
            data.popleft()
            break
        elif data.index(target[i]) <= len(data)//2:
            data.append(data.popleft())
            count += 1
        elif data.index(target[i]) > len(data)//2:
            data.appendleft(data.pop())
            count += 1
print(count)