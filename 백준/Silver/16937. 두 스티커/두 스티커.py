import sys

h, w = map(int, input().split())
n = int(input())
stickers = []
for _ in range(n):
    r, c = map(int, input().split())
    if (r > h and r > w) or (c > h and c > w): # 스티커의 길이가 모눈종이의 길이보다 작은지 유효성 검사사
        continue
    stickers.append([r, c])

n = len(stickers) # 유효성 검사를 거친 후, n 값 수정
answer = 0

for i in range(n):
    r1, c1 = stickers[i][0], stickers[i][1]
    for j in range(i+1, n):
        r2, c2 = stickers[j][0], stickers[j][1]
            
        # 두 스티커를 가로로 이어 붙일 때
        if (r1 + r2 <= w and max(c1, c2) <= h) or \
        (r1 + c2 <= w and max(c1, r2) <= h) or \
        (c1 + r2 <= w and max(r1, c2) <= h) or \
        (c1 + c2 <= w and max(r1, r2) <= h):
            answer = max(answer, r1 * c1 + r2 * c2)
             
        # 두 스티커를 세로로 이어 붙일 때
        elif (r1 + r2 <= h and max(c1, c2) <= w) or \
        (r1 + c2 <= h and max(c1, r2) <= w) or \
        (c1 + r2 <= h and max(r1, c2) <= w) or \
        (c1 + c2 <= h and max(r1, r2) <= w):
            answer = max(answer, r1 * c1 + r2 * c2)

print(answer)
                