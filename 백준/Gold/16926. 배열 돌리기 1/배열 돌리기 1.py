import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N, M, R = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    answer = [[0] * M for _ in range(N)]
    layers = min(N, M) // 2

    for k in range(layers):
        queue = deque()
        
        # 윗변 (좌 -> 우)
        for j in range(k, M - k):
            queue.append(matrix[k][j])
        # 우측변 (상 -> 하, 중복 모서리 제외)
        for i in range(k + 1, N - k - 1):
            queue.append(matrix[i][M - 1 - k])
        # 밑변 (우 -> 좌, k번째 행)
        for j in range(M - 1 - k, k - 1, -1):
            queue.append(matrix[N - 1 - k][j])
        # 좌측변 (하 -> 상, 중복 모서리 제외)
        for i in range(N - 2 - k, k, -1):
            queue.append(matrix[i][k])
            
        queue.rotate(-R)
        
        # 윗변
        for j in range(k, M - k):
            answer[k][j] = queue.popleft()
        # 우측변
        for i in range(k + 1, N - k - 1):
            answer[i][M - 1 - k] = queue.popleft()
        # 밑변
        for j in range(M - 1 - k, k - 1, -1):
            answer[N - 1 - k][j] = queue.popleft()
        # 좌측변
        for i in range(N - 2 - k, k, -1):
            answer[i][k] = queue.popleft()

    # 출력
    for row in answer:
        print(*(row))

solve()