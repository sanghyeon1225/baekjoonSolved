from collections import deque

n, m, r = map(int, input().split())

data = [list(map(int, input().split()))for _ in range(n)]

layer = min(n, m) // 2

for k in range(layer):
    deq = deque()   
    top, left = k, k
    bottom, right = n - 1 - k, m - 1 - k
    
    # 왼, 아, 오, 위 순서대로 돌면서 deq에 추가하고
    # rotate 돌린다
    # 그 후 data를 다시 수정해준다
    
    # 왼
    for i in range(top, bottom):
        deq.append(data[i][left])
    
    # 아
    for i in range(left, right):
        deq.append(data[bottom][i])
    
    # 오
    for i in range(bottom, top, -1):
        deq.append(data[i][right])

    # 위
    for i in range(right, left, -1):
        deq.append(data[top][i])
    
    deq.rotate(r)
    
    # 왼
    for i in range(top, bottom):
        data[i][left] = deq.popleft()
    # 아
    for i in range(left, right):
        data[bottom][i] = deq.popleft()
    
    # 오
    for i in range(bottom, top, -1):
        data[i][right] = deq.popleft()

    # 위
    for i in range(right, left, -1):
        data[top][i] = deq.popleft()

for d in data:
    print(*d)