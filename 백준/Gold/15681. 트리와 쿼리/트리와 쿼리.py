import sys
sys.setrecursionlimit(10**5)

N, R, Q = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(N - 1)]
qs = [int(input()) for _ in range(Q)]

def solution(N, R, Q, edges, qs):
    
    adj = [[] for _ in range(N + 1)]
    for edge in edges:
        u, v = edge
        adj[u].append(v)
        adj[v].append(u)
        
    dp = [0 for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    
    # 서브트리의 크기를 메모제이션 <- 트리가 바뀌지 않기 때문
    def dpf(cur, par):
        
        if dp[cur] != 0:
            return dp[cur]

        dp[cur] = 1 # 초기값
        visited[cur] = True # 방문
        
        for nxt in adj[cur]:
            if not visited[nxt]:
                dp[cur] += dpf(nxt, cur)
        
        return dp[cur]
    
    dpf(R, -1)
    
    for q in qs:
        print(dp[q])
    
solution(N, R, Q, edges, qs)