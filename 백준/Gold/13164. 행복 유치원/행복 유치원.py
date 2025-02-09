n,k = map(int,input().split())
heights = list(map(int, input().split()))

height_diff = []
answer = 0

for i in range(n-1):
    height_diff.append(heights[i+1] - heights[i])

height_diff.sort()

for i in range(n-k):
    answer += height_diff[i]

print(answer)