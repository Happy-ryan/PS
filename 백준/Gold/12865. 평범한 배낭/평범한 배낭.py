n, k = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)]

def solution(n, k, infos):

    # 냅색
    # 행 : 가방(item - 인덱스)
    # 열 : 무게
    # 아이템 : 가치
    # dp[i][j] = max(dp[i][j], dp[i][j - w] + v) 
    # dp[i - 1][j] 가 맞지 않아? 그 전 행을 그대로 복사하기 때문에 dp[i - 1][j] = dp[i][j] 동일한 값을 가지게 된다.
    inf = int(1e18)
    # k 무게 초과는 볼 필요가 없음 / 행 : 첫번째 가방 선택~
    dp = [[-inf for _ in range(k + 1)] for _ in range(n + 1)]
    # 1. 기초셋팅
    dp[0][0] = 0
    # dp에서 행을 n + 1로 했음
    # 0base -> 1base
    infos = [[0, 0]] + infos
    
    for i in range(1, n + 1): 
        w, v = infos[i] # 0base -> 1base
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j] #1base
            if j - w >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)
    
    answer = -inf
    
    for i in range(1, n + 1):
        answer = max(answer, max(dp[i]))
        
    return answer

# 결론 : dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v) 
print(solution(n, k, infos))