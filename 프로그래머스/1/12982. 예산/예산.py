def solution(d, budget):
    d.sort()
    left = budget
    result = 0
    for i in d:
        if i <= left:
            result += 1
            left -= i
    return result