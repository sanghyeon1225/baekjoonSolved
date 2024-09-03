def solution(s):
    answer = ''
    str = len(s) // 2
    # 5글자면 5//2 > 2 abcde 2
    # 6글자면 6//2 > 3 abcdef 23
    if len(s) % 2 == 0:
        answer += s[str-1:str+1]
    else:
        answer += s[str]
    return answer