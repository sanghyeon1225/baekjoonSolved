import sys
from collections import deque

test = int(sys.stdin.readline())

for i in range(test):
    command = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    data = sys.stdin.readline()[1:-2].split(",")
    q = deque([])
    is_reverse = False
    count = 0
    
    for i in data:
        q.append(i)
    
    for i in command:
        if i == "D":
            count += 1
    if count > n:
        print("error")
        continue
    
    for i in command:
        if i == "R":
            if is_reverse:
                is_reverse = False
            else:
                is_reverse = True
        elif i == "D":
            if is_reverse:
                q.pop()
            else:
                q.popleft()
                
    if is_reverse:
        q.reverse()
    print("[", ",".join(list(q)), "]", sep="")
    