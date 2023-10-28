n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

# dp[i]: 비용이 i일 때 지울 수 있는 메모리의 최대 크기
# 왜 기준으로 cost를 선택했냐? 
# 메모리기준 dp[i]: 메모리가 i일 때 최소 비용
# 메모리는 10,000,000 길이 배열이 필요함
# M 10,000,000 최대 확보해야하는 메모리의 최대 크기
# N * M
# N 100개 각갹의 메모리 10,000,000
# M 10,000,000
max_cost = 10004;
dp = [-1] * max_cost
dp[0] = 0

for memory, cost in zip(memories, costs):
    for i in reversed(range(cost, max_cost)):
        if dp[i-cost] != -1:
            dp[i] = max(dp[i], dp[i-cost]+memory)

for i in range(max_cost):
    if dp[i] >= m:
        print(i)
        break