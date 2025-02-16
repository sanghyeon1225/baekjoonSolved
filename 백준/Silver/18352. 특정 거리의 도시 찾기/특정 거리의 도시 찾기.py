from collections import deque
import sys

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)
            
n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

BFS(graph, x, visited)

count = 0
for i in range(n+1):
    if visited[i] == k:
        print(i)
        count += 1
        
if (count == 0):
    print(-1)