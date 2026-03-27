import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())

data = []

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if (len(s) < m):
        continue
    data.append(s)

data_count = Counter(data)

sorted_data = sorted(data_count.items(), key=lambda x: (-x[1], -len(x[0]) , x[0]))    

for word in sorted_data:
    print(word[0])