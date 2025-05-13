def min_coins(n):
    # 5원짜리 동전을 최대한 사용
    max_five = n // 5
    for five in range(max_five, -1, -1):
        remainder = n - 5 * five
        if remainder % 2 == 0:
            two = remainder // 2
            return five + two
    return -1  # 2원과 5원으로 구성 불가능한 경우 (이 문제에서는 없음)

n = int(input())
answer = min_coins(n)
print(answer)
