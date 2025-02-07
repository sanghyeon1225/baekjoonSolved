n, k = map(int, input().split())
data = list(input())
answer = 0

for i in range(n):
    if data[i] == 'P':
        for j in range(max(0, i - k), min(n, i + k + 1)):
            if data[j] == 'H':
                data[j] = 'X'
                answer += 1
                break

print(answer)