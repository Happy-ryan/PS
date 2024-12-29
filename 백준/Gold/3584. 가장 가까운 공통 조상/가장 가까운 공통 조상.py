import sys
sys.setrecursionlimit(10**5)

t = int(input())

def solution(n, nodes, node1, node2):
    # 트리 구성
    adj = [[] for _ in range(n + 1)]
    for a, b in nodes:
        adj[a].append(b)
    # 트리 문제 - par 배열
    par = [0] * (n + 1)
    for p, c in nodes:
        par[c] = p
        
    
    # par 배열을 활용하여 부모 찾기
    node1_par = []
    node2_par = []
    def dfs(cur, node_par):
        visited[cur] = True
        
        if not visited[par[cur]]:
            dfs(par[cur], node_par)
            node_par.append(par[cur])


    # print(par)
    visited = [False] * (n + 1)
    dfs(node1, node1_par)
    node1_par.append(node1)
    # print(node1_par)
    visited = [False] * (n + 1)
    dfs(node2, node2_par)
    node2_par.append(node2)
    # print(node2_par)
    
    l = min(len(node1_par), len(node2_par))
    lca = 0
    for idx in range(l):
        if node1_par[idx] == node2_par[idx]:
            lca = node1_par[idx]
            
    return lca
    

for _ in range(t):
    n = int(input())
    nodes = [list(map(int, input().split())) for _ in range(n - 1)]
    node1, node2 = map(int, input().split())
    print(solution(n, nodes, node1, node2))
    