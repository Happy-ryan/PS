n, m = map(int, input().split())

from collections import deque

def solution(n, m):
    MAX_N = 100000
    in_queue = [False for _ in range(MAX_N + 1)]
    inf = int(1e9)
    def in_range(x):
        return 0 <= x < MAX_N + 1
    
    def bfs(x):
        dist = [inf for _ in range(MAX_N + 1)]
        dp = [0 for _ in range(MAX_N + 1)]
        
        dq = deque([])
        
        dq.append(x)
        in_queue[x] = True
        dist[x] = 0
        dp[x] = 1
        
        while dq:
            cx = dq.popleft()
            for k in [-1, 1, 2]:
                
                if k == 2:
                    nx = cx * k
                else:
                    nx = cx + k
                # 첫 도착
                if in_range(nx) and not in_queue[nx]:
                    dq.append(nx)
                    in_queue[nx] = True
                    dist[nx] = dist[cx] + 1
                    dp[nx] += dp[cx]
                # 도착은 이미 했는데 첫 도착이랑 거리가 같은 경우
                # 경우의 수에 추가를 해야힘!!
                elif in_range(nx) and in_queue[nx] and dist[nx] == dist[cx] + 1:
                    dp[nx] += dp[cx]
        
        return dist[m], dp[m]
    ans = bfs(n)
    return f"{ans[0]}\n{ans[1]} "
    
    
print(solution(n, m))