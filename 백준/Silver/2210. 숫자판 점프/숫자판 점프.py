def check_valid(nx, ny):
    if (nx < 0 or ny < 0 or nx >= 5 or ny >= 5):
        return False
    else:
        return True
    
def dfs(i, j, num, count):
    if count == 5: # 시행 횟수가 5번이 됐다면 정답을 입력하고 종료.
        answer.append(num)
        return
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(len(dx)): # dfs 구현
        nx = i + dx[k]
        ny = j + dy[k]
        if check_valid(nx, ny): # 이동한 범위가 유효한지 판단
            dfs(nx, ny, num + board[nx][ny], count + 1)
        else:
            continue    

board = [] # 숫자판 입력 받기 5 x 5 크기
answer= [] # 정답 저장

for _ in range(5):
  board.append(list(map(str, input().split())))

for i in range(5):
    for j in range(5):
        count = 0
        dfs(i, j, board[i][j], count)

print(len(set(answer)))