def hanoi(n, start, end, middle):
    if n == 1:
        move(start, end)
        return
    else:
        hanoi(n-1, start, middle, end)
        move(start, end)
        hanoi(n-1, middle, end, start)

def move(start, end):
    print(start, end)

n = int(input())

if n == 1:
    print(1)
else:
    print(2 ** n - 1)
hanoi(n, 1, 3, 2)