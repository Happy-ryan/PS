# https://www.acmicpc.net/problem/17404
# 선택하지 못하는 곳을 Inf로 두면 어짜피 최소 비용을 구해야하므로 특정 부분을 선택하냐 마느냐 고민할 필요가 없다.
from pprint import pprint

n = int(input())
costs = [list(map(int, input().split())) for row in range(n)]

def solution(costs):
    n = len(costs)
    inf = int(1e8)
    # 첫 번째 방에 따라서 N번방의 선택도 달라짐!
    first_room = [[costs[0][0], inf, inf],
                [inf, costs[0][1], inf],
                [inf, inf, costs[0][2]]]
    ans = inf
    for idx, first_cost in enumerate(first_room):
        dp = [[0, 0, 0] for row in range(n + 1)]
        dp[1][0], dp[1][1], dp[1][2] = first_cost
        for i in range(2, n + 1):
            dp[i][0] = costs[i - 1][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i - 1][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i - 1][2] + min(dp[i - 1][0], dp[i - 1][1])
        dp[n][idx] = inf # 첫 번째 방에서 0 번째 칸 선택시 N번방에서는 0 번째 선택 불가 <- 이 문제의 포인트, 인덱스로 접근
        ans = min(ans, min(dp[n]))
    return ans

print(solution(costs))