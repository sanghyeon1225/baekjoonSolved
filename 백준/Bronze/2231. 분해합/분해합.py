n = int(input())

count = 0

for i in range(1, n + 1):
    if i + sum(map(int, str(i))) == n:
        print(i)
        count += 1
        break
if(count == 0):
    print(0)