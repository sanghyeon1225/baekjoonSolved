n = int(input())
card = set(map(int, input().split()))  # set으로 변환

m = int(input())
find_card = list(map(int, input().split()))

answer = [1 if x in card else 0 for x in find_card]

print(*answer)
