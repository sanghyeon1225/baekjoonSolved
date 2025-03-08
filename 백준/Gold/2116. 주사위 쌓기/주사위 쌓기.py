n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
max_num = 0

def find_num(idx, j):
    global dices
    global top
    if idx == 0 or idx == 5:
        if idx == 0:
            top = dices[j][5]
        else:
            top = dices[j][0]
        return max(dices[j][1], dices[j][2], dices[j][3], dices[j][4])
    elif idx == 1 or idx == 3:
        if idx == 1:
            top = dices[j][3]
        else:
            top = dices[j][1]
        return max(dices[j][0], dices[j][2], dices[j][4], dices[j][5])
    elif idx == 2 or idx == 4:
        if idx == 2:
            top = dices[j][4]
        else:
            top = dices[j][2]
        return max(dices[j][3], dices[j][5], dices[j][0], dices[j][1])
    
for i in range(6):
    num = 0
    top = 0
    num += find_num(i, 0)
    for j in range(1, len(dices)):
        num += find_num(dices[j].index(top), j)
    max_num = max(max_num, num)

print(max_num)