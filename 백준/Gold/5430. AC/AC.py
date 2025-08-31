import sys
from collections import deque

test = int(sys.stdin.readline())

for i in range(test):
    command = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    q = deque(sys.stdin.readline().strip()[1:-1].split(","))
    is_reverse = False
    
    if command.count("D") > n:
        print("error")
        continue 
    
    for i in command:
        if i == "R":
            is_reverse = not is_reverse
        elif i == "D":
            if is_reverse:
                q.pop()
            else:
                q.popleft()
                
    if is_reverse:
        q.reverse()
    print("[" + ",".join(q) + "]")
    