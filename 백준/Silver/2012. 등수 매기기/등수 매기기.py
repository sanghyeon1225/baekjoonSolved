import sys

n = int(sys.stdin.readline())

rank = []

for _ in range(n):
    rank.append(int(sys.stdin.readline()))
    
rank.sort()
diff = 0
for i in range(n):
    diff += abs(rank[i] - (i+1))

print(diff)