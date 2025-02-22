n = int(input())
board = [list(input()) for _ in range(n)]
answer = 1

def check_board():
    global answer
    for i in range(n):
        row_count = 1  
        col_count = 1  

        for j in range(n - 1):
            # 행 검사
            if board[i][j] == board[i][j+1]:
                row_count += 1
            else:
                row_count = 1

            # 열 검사
            if board[j][i] == board[j+1][i]:
                col_count += 1
            else:
                col_count = 1

            answer = max(answer, row_count, col_count)


dx = [0, 1] # 오른쪽 방향으로 순차적으로 탐색하므로 왼쪽, 위쪽 방향은 구하지 않음
dy = [1, 0]

for i in range(n):
    for j in range(n):
        currentColor = board[i][j]
        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]
            if n > nx >= 0 and n > ny >= 0 and currentColor != board[nx][ny]:
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
                check_board()
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j]

print(answer)
       
