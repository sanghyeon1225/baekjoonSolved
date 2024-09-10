def solution(n, m):
    #약수 구하기
    small = []
    small_n = []
    small_m = []
    for i in range(1, n+1):
        if n % i == 0:
            small_n.append(i)
    for i in range(1, m+1):
        if m % i == 0:
            small_m.append(i)
    #최대공약수 구하기
    for i in range(len(small_n)):
        for j in range(len(small_m)):
            if (small_n[i] == small_m[j]):
                small.append(small_m[j])
    small = small[-1]
    #배수 구하기
    big = 0
    for i in range(max(n,m), n*m+1):
        if i % n == 0 and i % m == 0:
            big = i
            break
    return [small, big]