n = int(input())
k = int(input())
data = list(map(int, input().split()))
if(n <= k):
    print(0)
else:
    data.sort()

    diff = []

    for i in range(len(data)-1):
        diff.append(data[i+1] - data[i])

    diff.sort()
    
    for i in range(k-1):
        diff.pop()
        
    print(sum(diff))