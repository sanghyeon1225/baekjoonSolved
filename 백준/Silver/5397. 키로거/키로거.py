import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n):
    data = sys.stdin.readline().rstrip()
    left = deque([])
    right = deque([])
    for i in range(len(data)):
        if data[i] == "<":
            if left:
                right.append(left.pop())
        elif data[i] == ">":
            if right:
                left.append(right.pop())
        elif data[i] == "-":
            if left:
                left.pop()
        else:
            left.append(data[i])
    right.reverse()
    print("".join(left + right))
    