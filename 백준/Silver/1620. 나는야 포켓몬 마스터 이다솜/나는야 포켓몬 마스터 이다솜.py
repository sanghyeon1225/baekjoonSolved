import sys

n, m = map(int, sys.stdin.readline().split())

data = dict()

data2 = dict()
for i in range(1, n + 1):
    pokemon = sys.stdin.readline().rstrip()
    data[i] = pokemon
    data2[pokemon] = (i)

for _ in range(m):
    query = sys.stdin.readline().rstrip()
    
    if query.isdigit(): 
        print(data[int(query)]) 
    else: 
        print(data2[query])