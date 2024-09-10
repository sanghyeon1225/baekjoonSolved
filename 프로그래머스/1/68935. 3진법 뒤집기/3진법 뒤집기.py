def solution(n):
    number = ''
    while(n > 0):
        number += str(n % 3)
        n //= 3
    return int(number, 3)