# https://www.acmicpc.net/problem/7044

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
        return parent[x]
    return x


def union(parent, a, b):
    pa = find(parent, a)
    pb = find(parent, b)
    if pa == pb:
        return False
    parent[pa] = pb
    return True

def merge(adj, n):
    flag = False
    adj.sort(key=lambda x:x[2])
    parent = [i for i in range(n + 1)]
    sum_val = 0
    cnt = 0
    for v, u, cost in adj:
        if cnt == n - 1:
            flag = True
            break
        if union(parent, v, u):
            cnt += 1
            sum_val += cost
    if not flag:
        return -1
    return -sum_val

n, m = map(int, input().split())
adj = []
for _ in range(m):
    v, u, cost = map(int, input().split())
    adj.append((v, u, -cost))
    
print(merge(adj, n))