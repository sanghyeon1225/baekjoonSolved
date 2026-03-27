import sys
import math

n = int(sys.stdin.readline())
query = list(map(int, sys.stdin.readline().split()))

# 1. 0! 부터 20! 까지 미리 계산해두기 (시간 단축 핵심)
fact = [math.factorial(i) for i in range(21)]

# 2. 1부터 N까지 아직 안 쓴 숫자들을 모아두는 리스트
nums = list(range(1, n + 1)) 

# [문제 1] K번째 순열 찾기
if query[0] == 1:
    k = query[1] - 1  # ⭐️ 핵심: 딱 떨어지는 계산을 위해 k를 0번째(인덱스) 기준으로 맞춤
    answer = []
    
    for i in range(n, 0, -1): # 남은 자리수가 N개, N-1개... 1개가 될 때까지 반복
        # 남은 자리수(i-1)로 만들 수 있는 팩토리얼 덩어리 개수로 나눔
        idx = k // fact[i - 1] 
        
        answer.append(nums[idx]) # 해당 인덱스의 숫자를 정답에 추가
        nums.pop(idx)            # 쓴 숫자는 리스트에서 삭제
        k %= fact[i - 1]         # 다음 자리를 위해 나머지 갱신
        
    print(*answer) # 괄호 벗겨서 출력

# [문제 2] 주어진 순열이 몇 번째인지 찾기
else:
    target = query[1:]
    answer = 1 # 1번째부터 시작
    
    for i in range(n):
        # 내가 찾으려는 숫자가 남은 숫자들 중에서 몇 번째로 작은지 인덱스를 찾음
        idx = nums.index(target[i])
        
        # 내 앞을 지나간 '팩토리얼 덩어리' 개수만큼 정답에 더해서 건너뜀
        answer += idx * fact[n - 1 - i]
        nums.pop(idx) # 쓴 숫자는 삭제
        
    print(answer)