def solution(n):
    list = []
    while (n != 0):
        list.append(n % 10)
        n = n // 10
    return list