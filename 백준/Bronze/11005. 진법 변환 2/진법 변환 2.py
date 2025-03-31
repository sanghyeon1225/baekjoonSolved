a, b = map(int, input().split())
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = []

while a > 0:
    result.append(number[a % b])    
    a //= b

answer = ''.join(result[::-1])

print(answer)