n = int(input())
graphes = [int(input()) for _ in range(n)]

def solution(n, graphes):
    # 핵심: 연속으로 된 3잔은 마실 수 없음!!
    # 문제: 최대로 마실 수 있는 포도주의 양
    
    # 1. 완탐이 가능한가? 불가능. 왜? n이 10,000이므로 For문이 2번만 해도 간당간당함.
    # 2.   그리디인가? 
    #      DP인가? 앞에 마신 것이 뒤에 영향을 미침..작은 부분 > 큰 부분
    #      BFS(DFS)인가?(X) > 그래프적 접근 어려움.
    #      우선순위 큐인가? > 순서가 중요하기 때문에 우선순위 큐로 접근하면 안돼
    
    # DP로 문제를 정의 > DP의 정의가 필요하다.
    # DP[i]: i번째 와인을 반드시 섭취한다고 했을 경우, 최대 와인의 양은 얼마인가?
    # 3번 연속으로 마실 수 없으므로 바로 i - 1 번째 와인을 마셨는가 안마셨는가로 확인해야함.
    # dp[i] = max(graphes[i] + dp[i - 1] + dp[i - 3]
    #             graphes[i] + dp[i - 2])
    
    # 틀린이유: i번째 와인을 반드시 섭취에서 '반드시'가 틀렸다.
    # 왜냐하면 100 100 0 이면 3번째 와인을 선택하는 곳에서는 선택을 안하는게 맞다.
    # 왜냐하면 선택하면 100밖에 못먹는에 선택안하면 200을 먹을 수 있으므로.
    # dp[i] i번째 와인 위치에서의 최대값 <- i번째 와인이 섭취 가능 or 안함!

    inf = int(1e18)
    graphes = [0] + graphes
    dp = [-inf for _ in range(n + 1)]
    
    dp[0] = 0
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = graphes[i]
        if i == 2:
            dp[i] = dp[i - 1] + graphes[i]
        # i번째 와인이 너무 작아서 선택하면 손해야!! 그래서 나는 i번째 와인은 거른다!
        if i >= 1:
            dp[i] = max(dp[i], dp[i - 1])
        # i번째 와인은 먹을거야. 그런데 바로 옆 i - 1은 모르겠어.
        if i >= 2:
            dp[i]  = max(dp[i], graphes[i] + dp[i - 2])
        if i >= 3:
            dp[i] = max(dp[i], graphes[i] + graphes[i - 1] + dp[i - 3])
            
    return max(dp)

print(solution(n, graphes))