num = int(input())
answer = 0

while(num >= 0):
    if num % 5 == 0:
        answer += (num // 5)
        print(answer)
        break
    num -= 3
    answer += 1
else:
    print(-1)