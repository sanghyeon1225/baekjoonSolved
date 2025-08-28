n, k = map(int, input().split())

answer = []
index = 0
people = [i+1 for i in range(n)]

for i in range(n):
    index = (index + k - 1) % len(people)
    answer.append(people.pop(index))

print('<' + str(answer)[1:-1] + '>')