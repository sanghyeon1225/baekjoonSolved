def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


start = int(input())
end = int(input())
num = []

for i in range(start, end + 1):
    if is_prime(i):
        num.append(i)
        
if (len(num) == 0):
    print(-1)
else:
    print(sum(num))
    print(num[0])