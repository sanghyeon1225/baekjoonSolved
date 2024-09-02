def solution(x):
    answer = True
    check = 0
    a = x
    while(a != 0):
        check += a % 10
        a = a // 10
    if (x % check == 0):
        return answer
    else:
        return False
