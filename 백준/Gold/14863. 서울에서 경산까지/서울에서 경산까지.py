N, K = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(N)]

def soltuion(N, K, infos):
    
    # 행 - 구간1,2...
    # 열 - 시간
    # 아이템 - 돈
    
    inf = int(1e18)
    dp = [[-inf for _ in range(K + 1)] for _ in range(N + 1)] # 시간 K까지만 보면 된다.
    
    # 기초
    dp[0][0] = 0
    infos = [[0, 0, 0, 0]] + infos # 0base -> 1base
    # dp[i][j] = [max|min](dp[i][j], dp[i - 1][j - w] + v) : 점화식
    for i in range(1, N + 1):
        t1, money1, t2, money2 = infos[i]
        for j in range(K + 1):
            # dp[i][j] = dp[i - 1][j] <= 반드시 선택해야하므로 제외
            if j - t1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - t1] + money1)
            if j - t2 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - t2] + money2)
    
    
    return max(dp[N]) # K 이내 시간 중 최대 금액 # 구간을 모두 가긴 해야함,
        
print(soltuion(N, K, infos))