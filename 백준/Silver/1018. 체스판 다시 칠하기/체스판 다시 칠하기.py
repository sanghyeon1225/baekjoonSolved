def check_board(x, y):
    b_count = 0
    w_count = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if board[x + i][y + j] != 'B':
                    b_count += 1
                elif board[x + i][y + j] != 'W':
                    w_count += 1
            else:
                if board[x + i][y + j] != 'W':
                    b_count += 1
                elif board[x + i][y + j] != 'B':
                    w_count += 1
    return min(b_count, w_count)

n, m = map(int, input().split())

board = [input() for _ in range(n)]

min_count = []
for i in range(n - 7):
    for j in range(m - 7):
        min_count.append(check_board(i, j))

print(min((min_count)))
