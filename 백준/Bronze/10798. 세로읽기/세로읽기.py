import sys

str = []
for i in range(5):
    s = sys.stdin.readline().strip()
    str.append(s)

for i in range(15):
    for j in str:
        if i < len(j):
            print(j[i], end="")
    