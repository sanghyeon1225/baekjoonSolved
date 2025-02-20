clockNum = []
for i in range(1111, 10000):
    i = str(i)
    if '0' not in i:
        check = []
        for j in range(4):
            temp = int(i[j:] + i[:j])
            check.append(temp)
        if min(check) not in clockNum:
            clockNum.append(min(check))

inputNum = ''.join(input().split())
inputClock = []
for i in range(4):
    temp = int(inputNum[i:] + inputNum[:i])
    inputClock.append(temp)
print(clockNum.index(min(inputClock)) + 1)
