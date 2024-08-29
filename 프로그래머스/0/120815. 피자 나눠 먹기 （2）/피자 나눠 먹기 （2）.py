def solution(n):
    for i in range(1, 10000):
        if 6 * i % n == 0: 
            return i
    