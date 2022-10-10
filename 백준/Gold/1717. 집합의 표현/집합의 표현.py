import sys
sys.setrecursionlimit(10**5)

n,m = map(int,input().split())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x


def union(a,b):
    pa = find(a)
    pb = find(b)
    parent[pa] = pb

for _ in range(m):
    c,a,b = map(int,input().split())
    if c == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
