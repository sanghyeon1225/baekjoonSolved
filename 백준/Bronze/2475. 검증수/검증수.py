data = list(map(int, input().split()))

answer = 0

for num in data:
    answer += num * num
    
print(answer % 10)