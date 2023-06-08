# https://www.acmicpc.net/problem/1922

# -- 대표 노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
        return parent[x]
    return x

# -- 대표노드끼리 연결하기
def union(parent, a, b):
    pa = find(parent, a)
    pb = find(parent, b)
    if pa == pb:
        return False
    parent[pa] = pb
    return True
    

def solution(n, m, adj):
    # --1. 간선들의 가중치 순으로 오름차순 정렬
    adj.sort(key= lambda x: x[2])
    # --2. parent 초기화
    parent = [i for i in range(n + 1)]
    sum_val = 0
    cnt = 0
    for u, v, cost in adj:
        if cnt == n - 1:
            break
        if union(parent, u, v):
            sum_val += cost
            cnt += 1
    return sum_val


n = int(input())
m = int(input())
adj = []
for _ in range(m):
    v, u, cost = map(int, input().split())
    adj.append((v, u, cost))
    
print(solution(n, m, adj))