# https://www.acmicpc.net/problem/3584
import sys
sys.setrecursionlimit(10**5)

def solution(n, edges, two_node):
    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    pars = set()
    for edge in edges:
        par, son = edge
        pars.add(par)
        adj[par].append(son)
        radj[son].append(par)

    inf = int(1e18)

    def dfs(cur):
        visited[cur] = True
        prev.append(cur)

        for nxt in radj[cur]:
            if not visited[nxt]:
                dfs(nxt)

    prevs = []
    for node in two_node:
        visited = [False for _ in range(n + 1)]
        prev = []
        dfs(node)
        prevs.append(prev)

    frist_node_prev = prevs[0]
    second_node_prev = prevs[1]
    # print(frist_node_prev)
    # print(second_node_prev)
    ans = (inf, inf)
    for x in frist_node_prev:
        if x in second_node_prev:
            ans = min(ans, (frist_node_prev.index(x) + second_node_prev.index(x), x))
    
    return ans[1]


t = int(input())
for _ in range(t):
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    two_node = list(map(int, input().split()))
    print(solution(n, edges, two_node))

# 1
# 16
# 1 14
# 8 5
# 10 16
# 5 9
# 4 6
# 8 4
# 4 10
# 1 13
# 6 15
# 10 11
# 6 7
# 10 2
# 16 3
# 8 1
# 16 12
# 3 12

# 1
# 5
# 2 3
# 3 4
# 3 1
# 1 5
# 3 5
