def solution(left, right):
    #약수 갯수 1~i 까지 나눠서 0으로 떨어지면 count 추가
    sum = 0
    for i in range(left, right+1, 1):
        count = 0
        for j in range(1, i):
            if(i % j == 0):
                count += 1
        if count % 2 == 0:
            sum += i
        else:
            sum -= i
    return -sum