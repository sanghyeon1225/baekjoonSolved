a, b = input().split()
b = int(b)
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0

for i in range(len(a)):
    sum += number.index(a[-(i+1)]) * (b**i)
    
print(sum)


