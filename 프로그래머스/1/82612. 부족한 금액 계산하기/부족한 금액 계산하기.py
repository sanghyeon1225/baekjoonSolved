def solution(price, money, count):
    time = 0
    sum = 0
    for i in range(count):
        time += 1
        sum += price * time
    if (sum > money):
        return sum - money
    else:
        return 0