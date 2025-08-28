import sys

left = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())

cursor = []

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "L":
        if left:
            cursor.append(left.pop())
    elif command[0] == "D":
        if cursor:
            left.append(cursor.pop())
    elif command[0] == "B":
        if left:
            left.pop()
    elif command[0] == "P":
        left.append(command[1])
        
print("".join(left + cursor[::-1]))