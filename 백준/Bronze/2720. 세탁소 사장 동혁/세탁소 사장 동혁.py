iii = int(input())
data = []
for i in range(iii):
    data.append(int(input()))

q = 0
d = 0
n = 0
p = 0

for i in range(iii):
    q = 0
    d = 0
    n = 0
    p = 0
    
    money = data[i]
    q = money / 25
    money %= 25
    
    d = money / 10
    money %= 10
    
    n = money / 5
    money %= 5
    
    p = money / 1
    print(int(q), int(d), int(n), int(p))
    
    