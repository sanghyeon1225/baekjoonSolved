n = int(input())

rope = [int(input()) for _ in range(n)]

rope.sort(reverse=True)

max_weight = 0

for i in range(len(rope)):
    weight = rope[i] * (i+1)
    max_weight = max(weight, max_weight)

print(max_weight)