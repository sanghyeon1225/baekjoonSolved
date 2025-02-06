def check_valid(i, j, op):
    if op == '<':
        return i < j
    return i > j

def solve(depth, s):
    if depth == n + 1:
        answer.append(s)
        return
    for i in range(10):
        if visited[i] == 0: # 해당 숫자가 사용 됐는지 확인 (0이면 아직 사용되지 않은 것)
            if depth == 0 or check_valid(s[-1], str(i), op[depth - 1]): # 0~9까지 차례대로 접근
                visited[i] = 1
                solve(depth + 1, s + str(i)) # solve 함수를 재귀적으로 반복하여 정답 찾기
                visited[i] = 0 # 새로운 탐색을 위해 다시 초기화화

n = int(input()) # 부등호 개수 입력 받기
op = list(input().split()) # 전체 부등호 인자 입력 받기

visited = [0] * 10 # 사용된 숫자 체크 용도
answer = [] # 정답 저장 리스트

solve(0, "") # 함수 실행 (깊이 0, 문자열 초기값 공백으로 시작)

answer.sort() # 저장한 정답들을 크기 순서대로 정렬
 
print(answer[-1]) # 정답 중 가장 큰 수 출력
print(answer[0]) # 정답 중 가장 작은 수 출력
