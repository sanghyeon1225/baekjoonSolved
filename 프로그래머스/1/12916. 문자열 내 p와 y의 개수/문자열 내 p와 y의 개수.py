def solution(s):
    p = s.count('P') + s.count('p')
    y = s.count('Y') + s.count('y')
    if p == y:
        return True
    else:
        return False