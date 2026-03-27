import sys

n = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split()))  # 도로의 길이 (N-1개)
prices = list(map(int, sys.stdin.readline().split())) # 각 도시 주유소의 리터당 가격 (N개)

min_price = prices[0] # 첫 출발지에서는 선택권 없이 무조건 기름을 넣어야 함!
total_cost = 0        # 총 누적 주유 비용

# 3. 길을 따라가며 계산 (도시는 N개지만, 길은 N-1개이므로 반복문은 N-1번 돕니다)
for i in range(n - 1):
    # (1) 현재까지 발견한 '가장 싼 가격'으로 다음 도시까지 갈 만큼의 기름을 결제
    total_cost += min_price * roads[i]
    
    # (2) 다음 도시에 도착했는데, 거기 주유소가 지금 내가 아는 최저가보다 더 싸다면?
    if prices[i + 1] < min_price:
        min_price = prices[i + 1] # 최저가 갱신! (앞으로는 여기서 산 기름으로 달림)

# 4. 최종 누적 비용 출력
print(total_cost)