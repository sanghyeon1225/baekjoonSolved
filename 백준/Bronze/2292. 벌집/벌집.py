n = int(input())

count = 1
cycle = 1

while(n > cycle):
    cycle = count * 6 + cycle
    count += 1
print(count)