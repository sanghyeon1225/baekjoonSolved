import sys

n = int(sys.stdin.readline())
papers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False] * 100 for _ in range(100)]
count = 0
for paper in papers:
    x = paper[0]
    y = paper[1]
    
    for i in range(10):
        for j in range(10):
            if visited[x+i][y+j] == 0:
                visited[x+i][y+j] = 1
                count += 1

print(count)