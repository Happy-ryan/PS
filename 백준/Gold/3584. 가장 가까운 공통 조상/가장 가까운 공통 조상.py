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

    # 두 노드의 공통조상 노드 뒤부터는 전부 동일할 것
    # 공통조상이 4인데 4이후부터는 동일한 것 볼 수 있음!
    # [3, 16, 10, 4, 8]
    # [15, 6, 4, 8]
    tmp = -1
    while True:
        if abs(tmp) > min(len(frist_node_prev), len(second_node_prev)) or frist_node_prev[tmp] != second_node_prev[tmp]:
            return frist_node_prev[tmp + 1]
        tmp -= 1


t = int(input())
for _ in range(t):
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    two_node = list(map(int, input().split()))
    print(solution(n, edges, two_node))