import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque([])

for i in range(n):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push_front":
        q.appendleft(command[1])
    elif command[0] == "push_back":
        q.append(command[1])
    elif command[0] == "pop_front":
        print(q.popleft() if q else -1)
    elif command[0] == "pop_back":
        print(q.pop() if q else -1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(0 if q else 1)
    elif command[0] == "front":
        print(q[0] if q else -1)
    elif command[0] == "back":
        print(q[-1] if q else -1)

    