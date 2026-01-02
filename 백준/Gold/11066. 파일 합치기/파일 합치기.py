def solution(K, files):
    inf = int(1e9)
    
    # dp[i][j] = i번째부터 j번째 파일까지 합치는 최소 '비용'
    dp = [[0 for _ in range(K + 1)] for _ in range(K + 1)]
    
    # 구간 합 (i~j 파일을 한 번에 합칠 때의 비용)
    prefix_sum = [0] * (K + 1)
    for i in range(1, K + 1):
        prefix_sum[i] = prefix_sum[i - 1] + files[i - 1]
    
    # 구간 길이를 늘려가며 DP
    for length in range(2, K + 1):  # 구간 길이 2부터 K까지
        for i in range(1, K - length + 2):  # 시작 위치
            j = i + length - 1  # 끝 위치
            
            dp[i][j] = inf
            
            # i~j 구간을 k 지점에서 나누어 합치기
            for k in range(i, j):
                # [i~k] + [k+1~j] 로 나누어 합침
                cost = dp[i][k] + dp[k + 1][j] + (prefix_sum[j] - prefix_sum[i - 1])
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[1][K]

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    print(solution(K, files))