import sys

n = sys.stdin.readline().strip()
f = int(sys.stdin.readline().strip())

base_n = int(n[:-2] + "00")

for i in range(100):
    target = base_n + i
    if target % f == 0:
        print(f"{i:02d}")
        break