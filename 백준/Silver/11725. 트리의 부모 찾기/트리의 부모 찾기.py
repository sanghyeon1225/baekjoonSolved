import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for i in range(n - 1): # 간선을 입력 받아 노드 구성 확인
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(v):
    for i in tree[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)

def answer():
    for i in range(2, n+1):
        print(parent[i])
        
dfs(1)
answer()
