def solution(s):
    alp = []
    alp = s.split(" ")
    new_s = ""
    for i in range(len(alp)):
        for j in range(len(alp[i])):
            if j % 2 == 0:
                new_s += alp[i][j].upper()
            else:
                new_s += alp[i][j].lower()
        new_s += " "
    return new_s[:-1]