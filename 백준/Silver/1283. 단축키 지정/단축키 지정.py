def firstFind(i, j):
    global flag
    if options[i][j][0].isalpha():
        idx = ENG.index(options[i][j][0].upper())
        if visited[idx] == 0:
            visited[idx] = 1
            options[i][j] = "[" + options[i][j][0] + "]" + options[i][j][1:]
            flag = 1
    
def secondFind(i, j, k):
    global flag
    if options[i][j][k].isalpha():
        idx = ENG.index(options[i][j][k].upper())
        if visited[idx] == 0:
            visited[idx] = 1
            options[i][j] = options[i][j][:k] + "[" + options[i][j][k] + "]" + options[i][j][k+1:]
            flag = 1


n = int(input())
options = [input().split() for _ in range(n)]

ENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
visited = [0] * 26
for i in range(n):
    flag = 0
    for j in range(len(options[i])):
        if(flag == 0):
            firstFind(i, j)
    for j in range(len(options[i])):
        for k in range(len(options[i][j])):
            if(flag == 0):
                secondFind(i, j, k)
    
for option in options:
    print(' '.join(option))