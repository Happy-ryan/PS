import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solution(N, edges):
    
    adj = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)  # 양방향성
    
    
    # dp[i][0] = i번째 사람이 얼리어답터가 아닐 때 루트i 서브트리의 얼리어답터의 최소수
    # dp[i][1] = i번째 사람이 얼리어답터일 때 루트i 서브트리의 얼리어답터의 최소수
    
    # 점화식  dp[i][0] = dp[i's child][1] # 반드시 모두가 자식이 얼리어답터야함.
    
    #       dp[i][1] = 1(나 자신) + min(dp[i's child][0], dp[i's child][1])
    #                  그런데 i가 얼리어답터면 내 자식의 얼리어답터 유무 상관없으니 더 좋은거를 골라야함.
    
    # tree dp는 무조건 post_order 진행
    post_order = []
    inf = int(1e18)
    dp = [[inf for _ in range(2)] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    def post(root):
        
        # dp 종료
        if dp[root][0] != inf and dp[root][1] != inf:
            return # 이미 방문 완료
    
        visited[root] = True
        # dp 기초
        dp[root][0] = 0
        dp[root][1] = 1 # <- 내가 얼리어답터이므로 우선 기초 셋팅은 1
        
        for child in adj[root]:
            if not visited[child]:
                post(child)
                # 추포
                dp[root][0] += dp[child][1]
                dp[root][1] += min(dp[child][0], dp[child][1])
            
        post_order.append(root)
        
    root = 1
    post(root)
    
    return min(dp[root][0], dp[root][1])

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N - 1)]

print(solution(N, edges))
