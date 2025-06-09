def solution(mats, park):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if (park[i][j] != '-1'):
                park[i][j] = 0
            else:
                park[i][j] = 1
    
    mats.sort(reverse=True)
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if (i > 0 and j > 0 and park[i][j] == 1):
                park[i][j] = min(park[i-1][j], park[i][j-1], park[i-1][j-1]) + 1
    
    answer = max(max(row) for row in park)

    for i in mats:
        if i <= answer:
            return i
    
    return -1
    