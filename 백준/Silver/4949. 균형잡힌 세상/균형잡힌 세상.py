import sys

while(True):
    flag = True
    data = list(sys.stdin.readline().rstrip())
    if (len(data) == 1 and data[-1] == "."):
        exit(0)

    stack = []
    
    for i in range(len(data)):
        if data[i] in ("(", "["):
            stack.append(data[i])
        elif data[i] == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
        elif data[i] == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
    
    if flag and not stack:
        print("yes")
        continue
    else:
        print("no")
    
    
    