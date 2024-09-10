def solution(t, p):
    count = 0
    new_string = []
    for i in range(len(t)-len(p)+1):
        new_string.append(t[i:i+len(p)])
    for i in new_string:
        if int(i) <= int(p):
            count += 1
    return count