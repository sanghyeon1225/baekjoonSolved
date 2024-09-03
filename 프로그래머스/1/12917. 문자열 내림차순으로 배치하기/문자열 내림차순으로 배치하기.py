def solution(s):
    #대문자 65~
    #소문자 91~ 내림차순으로
    #ord() > 영어 > 숫자
    #chr() > 숫자 > 영어
    arr = []
    answer = ''
    for i in s:
        arr.append(ord(i))
    arr.sort(reverse=True)
    for i in arr:
        answer += chr(i)
    return answer