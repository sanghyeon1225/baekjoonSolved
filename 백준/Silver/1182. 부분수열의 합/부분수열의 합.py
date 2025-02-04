from itertools import combinations

n, s = map(int, input().split()) # 수열 속 정수의 개수 n, 타겟 넘버 s 입력 받기
number = list(map(int, input().split())) # 수열 값 입력 받기
answer = 0

for i in range(n):
    sub = list(combinations(number, i+1)) # combinations 함수를 이용하여 부분수열을 구함
    for j in range(len(sub)): 
        total = sum(sub[j]) 
        if s == total: # 부분수열의 합과 타겟 넘버가 같은지 확인
            answer = answer + 1
                        
print(answer)