def solution(a, b, c, d):
    # 같은거 4개 > 1111 x p
    # 같은거 3개 다른거 1개 > (10 × p + q)^2
    # 같은거 2개씩 (p + q) × |p - q|
    # 같은거 2개 1개씩 다름 q × r
    # 모두 다르면 가장 작은 수
    num = 0
    num1 = 0
    num2 = 0
    # 주사위 굴린수에 해당하는 인덱스 추가
    list = [0] * 7
    list[a] += 1
    list[b] += 1
    list[c] += 1
    list[d] += 1
    
    # 수 할당이 어떻게 됐는지 count
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    for i in range(7):
        if list[i] == 1:
            c1 += 1
        if list[i] == 2:
            c2 += 1
        if list[i] == 3:
            c3 += 1
        if list[i] == 4:
            c4 += 1

    if(c4 == 1):
        for i in range(7):
            if list[i] == 4:
                return i * 1111
            
    if(c3 == 1 and c1 == 1):
        for i in range(7):
            if list[i] == 3:
                num = i
            elif list[i] == 1:
                num2 = i
        return ((10 * num) + num2) ** 2
    
    
    if(c2 == 2):
        count = []
        for i in range(7):
            if list[i] == 2:
                count.append(i)
        num = count[0]
        num1 = count[1]
        return (num + num1) * abs(num - num1)
                                  
    if(c2 == 1 and c1 == 2):
        count = []
        for i in range(7):
            if list[i] == 1:
                count.append(i)
        return count[0] * count[1]
    
    if(c1 == 4):
        count = []
        for i in range(7):
            if list[i] == 1:
                count.append(i)
        return min(count)