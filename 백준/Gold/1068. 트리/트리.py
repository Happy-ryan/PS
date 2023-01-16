# 유형 : 특정 노드를 삭제 시켰을 때 리프노드의 수
import sys
input = sys.stdin.readline
n = int(input())
pars = list(map(int, input().split()))
d_node = int(input())

adj = [[] for _ in range(n)]
siz = [0] * n

for child, par in enumerate(pars):
    if par == -1: continue
    adj[par].append(child)

def dfs(cur):
    if cur == d_node:
        return
    siz[cur] = 1
    for nxt in adj[cur]:
        dfs(nxt)
        siz[cur] += siz[nxt]

root = pars.index(-1)
dfs(root)
print(siz.count(1))