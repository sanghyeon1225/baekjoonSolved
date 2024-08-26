def solution(a, b):
    a1 = int(str(a) + str(b))
    b1 = 2 * a * b
    if a1 >= b1:
        return a1
    else:
        return b1