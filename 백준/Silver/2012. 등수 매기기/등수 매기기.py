import sys

n = int(sys.stdin.readline())

rank = []

for _ in range(n):
    rank.append(int(sys.stdin.readline()))
    
rank.sort()
diff = 0
for i in range(1, n+1):
    diff += abs(rank[i-1] - i)

print(diff)