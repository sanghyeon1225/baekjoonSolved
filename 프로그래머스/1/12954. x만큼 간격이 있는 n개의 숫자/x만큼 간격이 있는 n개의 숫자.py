def solution(x, n):
    answer = []
    count = 1
    while(count <= n):
        answer.append(x * count)
        count += 1
    return answer