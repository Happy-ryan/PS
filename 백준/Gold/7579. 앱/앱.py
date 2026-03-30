N, M = map(int, input().split())
memorys = list(map(int, input().split()))
costs = list(map(int, input().split()))

def solution(N, M, memorys, costs):
    # M 이라는 메모리를 확보하기 위한 최소 비용
    # 아이템 - 비용(보통)
    # 행 - i번째 앱 선택
    # 열 - 메모리(보통)
    
    # 메모리 열...10,000,000 * 100 <- 너무 크다
    # 비용 열 ... 100 * 100
    # 비용이 c일 때 확보된 메모리(M) 
    
    # 아이템 - 메모리 / 열 - 비용
    inf = int(1e18)
    col = 100 * 100 + 1
    # inf : 메모리..최소비용으로 큰 메모리 넣어야 좋은 것,
    dp = [[-inf for _ in range(col)] for _ in range(N + 1)]
    
    # 기초
    dp[0][0] = 0
    memorys = [0] + memorys # 0base -> 1base
    costs = [0] + costs # 0base -> 1base
    # dp[i][j] = [max, min](dp[i][j], dp[i - 1][j - w] + v)
    for i in range(1, N + 1):
            c, m = costs[i], memorys[i]
            for j in range(col):
                dp[i][j] = dp[i - 1][j]
                if j - c >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - c] + m)
    
    # 비용 0부터 순회하며 처음으로 메모리 M을 넘기는 비용 찾기
    for cost in range(col + 1):
        if dp[N][cost] >= M:
            return cost
        
print(solution(N, M, memorys, costs))