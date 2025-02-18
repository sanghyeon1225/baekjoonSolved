from collections import deque
import sys

def BFS(start):
    isTree = True
    q = [start]
    while q:
        now = q.pop(0)
        if visited[now] == 1:
            isTree = False
        visited[now] = 1
        for j in graph[now]:
            if visited[j] == 0:
                q.append(j)
    return isTree

caseNumber = 0

while(True):
    caseNumber += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    visited = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m): # 간선 정보 추가
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    count = 0
    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        if BFS(i) is True:
            count += 1
    
    if count == 0:
        print(f"Case {caseNumber}: No trees.")
    elif count == 1:
        print(f"Case {caseNumber}: There is one tree.")
    else:
        print(f"Case {caseNumber}: A forest of {count} trees.")