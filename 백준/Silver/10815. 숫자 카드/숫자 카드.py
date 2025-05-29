def binary_search(target, data, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    
    if data[mid] == target:
        return 1
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
    
    return binary_search(target, data, start, end)

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
find_card = list(map(int, input().split()))

answer = []
for i in range(m):
    answer.append(binary_search(find_card[i], card, 0, n-1))

print(*answer)