import math

n = int(input())

data = [4]

for i in range(n):
    length = math.sqrt(data[i])
    length = length*2 - 1
    data.append(length**2)
    
print(int(data[n]))