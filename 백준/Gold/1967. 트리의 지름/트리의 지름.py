import sys
sys.setrecursionlimit(10**5)

n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    s, e, cost = map(int, input().split())
    adj[s].append((cost, e))
    adj[e].append((cost, s))
    
def solution():
    
    def dfs(cur, p): # 가장 먼 정점과 그 거리
        max_res = (0, cur)
        for cost, nxt in adj[cur]:
            if nxt == p:
                continue
            dist, target = dfs(nxt, cur)
            max_res = max(max_res, (dist + cost, target))
        return max_res

    _, root = dfs(1, None)
    dist, _ = dfs(root, None)
    return dist

print(solution())