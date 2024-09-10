def solution(array, commands):
    answer = []
    i = 0
    j = 0
    k = 0
    for a in commands:
        i = a[0]
        j = a[1]
        k = a[2]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer