n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    
    dist = y - x
    cur_dist = 0
    
    count = 0
    step = 1
    
    while cur_dist < dist:
        count += 1
        cur_dist += step
        
        if count % 2 == 0:
            step += 1
            
    print(count)
    