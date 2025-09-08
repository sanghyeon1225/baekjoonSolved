n = int(input())
count = 0

for _ in range(n):
    data = input()
    stack = []
    
    for i in data:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        elif stack[-1] != i:
            stack.append(i)
    
    if not stack:
        count += 1
    
print(count)