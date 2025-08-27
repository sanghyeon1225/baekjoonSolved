n, target = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            total = cards[i] + cards[j] + cards[k]
            if total <= target:
                max_sum = max(max_sum, total)
                
print(max_sum)