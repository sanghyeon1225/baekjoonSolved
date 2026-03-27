import sys

n = int(sys.stdin.readline())
answer = set() # 리스트 대신 set 사용

for _ in range(n):
    cmd = sys.stdin.readline().split()
    
    # 명령어가 1개인 경우 (all, empty)
    if len(cmd) == 1:
        if cmd[0] == "all":
            answer = set(range(1, 21))
        else: # empty
            answer = set()
        continue
    
    # 명령어가 2개인 경우
    command, target = cmd[0], int(cmd[1])
    
    if command == "add":
        answer.add(target) # set은 중복 추가를 알아서 무시함
    elif command == "remove":
        answer.discard(target) # remove와 달리 discard는 값이 없어도 에러를 내지 않음
    elif command == "check":
        if target in answer:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if target in answer:
            answer.discard(target)
        else:
            answer.add(target)