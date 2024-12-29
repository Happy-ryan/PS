import sys
sys.setrecursionlimit(10**5)

t = int(input())

def solution(n, edges, na, nb):
    # 트리 구성
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
    # 트리 문제 - par 배열
    par = [0] * (n + 1)
    for p, c in edges:
        par[c] = p
        
    
    # par 배열을 활용하여 부모 찾기
    node1_par = []
    node2_par = []
    # step = []
    
    def dfs(cur, node_par):
        visited[cur] = True
        # step.append(cur)
        
        if not visited[par[cur]]:
            dfs(par[cur], node_par)
            
        node_par.append(cur) # 나도 공통조상될 수 있음!


    # print(par)
    visited = [False] * (n + 1)
    visited[0] = True
    dfs(na, node1_par)

    # print(node1_par)
    visited = [False] * (n + 1)
    visited[0] = True
    dfs(nb, node2_par)

    # print(node2_par)
    
    l = min(len(node1_par), len(node2_par))
    lca = 0
    for idx in range(l):
        if node1_par[idx] == node2_par[idx]:
            lca = node1_par[idx]
            
    return lca
    

for _ in range(t):
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    na, nb = map(int, input().split())
    print(solution(n, edges, na, nb))