def solution(board, h, w):
    sol = board[h][w]
    n = len(board)
    count = 0
    dh = [0,0,1,-1]
    dw = [1,-1,0,0]
    h_check = []
    w_check = []
    for i in range(4):
        h_check.append(int(h+dh[i]))
        w_check.append(int(w+dw[i]))
        if (n > h_check[i] and h_check[i] >=0) and (n > w_check[i] and w_check[i] >=0):
            if sol == board[h_check[i]][w_check[i]]:
                count += 1
    return count