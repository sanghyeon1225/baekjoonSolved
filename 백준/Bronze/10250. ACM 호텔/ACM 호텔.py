n = int(input())
answer = []
for i in range(n):
    data = list(map(int, input().split()))

    if (data[2] % data[0] == 0):
        floor = str(data[0])
        room = str((data[2] // (data[0])))
    else:
        floor = str(data[2] % (data[0]))
        room = str((data[2] // (data[0])) + 1)
        
    if (len(room) == 1):
        answer.append(floor + '0' + room)
    else:
        answer.append(floor + room)

for i in range(n):
    print(answer[i])