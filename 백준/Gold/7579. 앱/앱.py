n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

def solution(n, m, memories, costs):
    # m = 10,000,000 / max_cost = 100 * 100
    # dp[i][j] i번째 앱(item)을 선택하고 j비용(weight) 일 때, 최대 메모리(value)의 값
    # 특정 비용일 때, 메모리를 최대한 비활성화 시키고 싶다!
    memories = [0] + memories
    costs = [0] + costs
    inf = int(1e9)
    max_cost = 100 * 100
    dp = [[-inf for _ in range(max_cost + 1)] for _ in range(n + 1)]
    
    dp[0][0] = 0
    for i in range(1, n + 1):
        w, v = costs[i], memories[i]
        for j in range(max_cost, -1, -1):
            dp[i][j] = dp[i - 1][j]
            if j - w >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)
    
    min_cost = inf
    # cost의 범위는 0 ~ 100 * 100d이다!!!!!!!!
    for cost in range(max_cost + 1):
        if dp[n][cost] >= m:
            min_cost = min(min_cost, cost)
            
    return min_cost


print(solution(n, m, memories, costs))