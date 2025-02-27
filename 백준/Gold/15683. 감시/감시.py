import copy
n, m = map(int, input().split())

origin_board = [list(map(int, input().split())) for _ in range(n)]
cctv_list = []
for i in range(n):
    for j in range(m):
        if 5 >= origin_board[i][j] >= 1:
            cctv_list.append((origin_board[i][j], i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mode = [[], 
        [[0], [1], [2], [3]], 
        [[0, 2], [1, 3]], 
        [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
        [[0, 1, 2, 3]]]

def checkMap(board):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1
    return count

def changeMap(x, y, mode, board):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx = nx + dx[i]
            ny = ny + dy[i]
            if not (n > nx >= 0 and m > ny >= 0):
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0: 
                board[nx][ny] = -1
    
def DFS(depth, board):
    global answer
    if depth == len(cctv_list):
        answer = min(answer, checkMap(board))
        return

    temp = copy.deepcopy(board)
    cctv_num, cctv_x, cctv_y = cctv_list[depth]
    
    for i in mode[cctv_num]:
        changeMap(cctv_x, cctv_y, i, temp)
        DFS(depth+1, temp)
        temp = copy.deepcopy(board)
        
answer = int(1e9)
DFS(0, origin_board)
print(answer)
