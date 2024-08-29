def solution(slice, n):
    for i in range(1,1000):
        if i * slice >= n :
            return i
        