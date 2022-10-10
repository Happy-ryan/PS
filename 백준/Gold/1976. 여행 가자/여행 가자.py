N = int(input())
M = int(input())
graph = [list(map(int,input().split())) for row in range(N)]
plan = list(map(int,input().split()))

par = [i for i in range(N+1)]

def find(x):
    if par[x] != x:
        par[x] = find(par[x])
        return par[x]
    return x

def union(a,b):
    pa = find(a)
    pb = find(b)
    par[pa] = pb

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1: # graph - 0 base
            union(r+1,c+1) # par - 1 base

res = set()
for i in plan:
    res.add(find(i))

if len(res) == 1:
    print('YES')
else:
    print('NO')