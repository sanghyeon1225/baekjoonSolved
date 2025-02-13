n = int(input())
vote = int(input())
data = list(map(int, input().split()))

pic = []
idx = []

for i in data:
    if i not in pic:
        if len(pic) >= n:
            min_idx = idx.index(min(idx)) # 추천이 제일 적은 후보 찾기
            del pic[min_idx]
            del idx[min_idx]    
        pic.append(i)
        idx.append(1)
    else:
        idx[pic.index(i)] += 1

pic.sort()
for i in pic:
    print(i, end=" ")
