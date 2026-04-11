T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    answer = 0
    for d in data:
        if d % 2 != 0:
            answer += d
    print(f"#{test_case+1} {answer}")