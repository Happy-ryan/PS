n, k = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)]

def solution(n, k, infos):
    # dp[i][j] i번째 물건 선택하고 무게j 일때, 최대 가치(value)
    infos = [0] + infos
    inf = int(1e9)
    dp = [[-inf for _ in range(k + 1)] for _ in range(n + 1)]
    
    # 
    dp[0][0] = 0
    for i in range(1, n + 1):
        w, v = infos[i]
        for j in range(k, -1, -1):
            dp[i][j] = dp[i - 1][j]
            if j - w >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)
    
    return max(dp[n])

print(solution(n, k, infos))