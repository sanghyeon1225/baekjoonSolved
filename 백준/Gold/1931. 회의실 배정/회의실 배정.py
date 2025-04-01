n = int(input())

meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

start = 0
count = 0 
for meeting in meetings:
    if (start <= meeting[0]):
        start = meeting[1]
        count += 1

print(count)