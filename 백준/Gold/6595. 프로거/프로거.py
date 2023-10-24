# https://www.acmicpc.net/problem/6595
import math

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
    adj.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    sum_val = set()
    cnt = 0
    for v, u, cost in adj:
        if find(parent, 1) == find(parent, 2):
            break
        if cnt == n - 1:
            break
        if union(parent, v, u):
            cnt += 1
            sum_val.add(cost)
    return sum_val

def cost(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    #dist = round(dist, 3)
    return dist

result = []
t = 1
while True:
    n = int(input())
    if n == 0:
        break
    adj = []
    coordinates = [0] + [list(map(int, input().split())) for _ in range(n)]
    for v in range(1, n + 1):
        for u in range(v + 1, n + 1):
            x1, y1 = coordinates[v]
            x2, y2 = coordinates[u]
            adj.append((v, u, cost(x1, y1, x2, y2)))
    input()
    frog_distance = max(merge(adj, n))
    # print(f"Scenario #{t}")
    # print(f"Frog Distance = {frog_distance:.3f}")
    res = f"Scenario #{t}\nFrog Distance = {frog_distance:.3f}"
    result.append(res)
    t += 1
    
for res in result[:-1]:
    print(res)
    print()
print(result[-1])