n = int(input())

for _ in range(n):
    data = input()
    stack = []
    
    for i in data:
        if not stack:
            stack.append(i)
        elif stack and stack[-1] != i:
            if stack[-1] == ")" and i == "(":
                stack.append(i) 
            stack.pop()
        elif stack and stack[-1] == i:
            stack.append(i)
    
    if stack:
        print("NO")
    else:
        print("YES")