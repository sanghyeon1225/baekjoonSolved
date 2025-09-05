from collections import deque

def bfs():
    global n, k
    visited[n] = True
    q = deque([(n, 0)])
    while(q):
        current, time = q.popleft()
        if current == k:
            return time

        for next in (current - 1, current + 1, current * 2):
            if 100000 >= next >= 0 and not visited[next]:
                q.append((next, time + 1))
                visited[next] = True
     
    

n, k = map(int, input().split())

visited = [False] * 100001

print(bfs())