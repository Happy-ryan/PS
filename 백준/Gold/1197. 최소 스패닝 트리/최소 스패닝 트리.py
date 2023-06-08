# https://www.acmicpc.net/problem/1197

# --1. 대표노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
        return parent[x]
    return x

# --2. 대표노드끼리 연결
def union(parent, a, b):
    pa = find(parent, a)
    pb = find(parent, b)
    if pa == pb:
        return False
    parent[pa]=pb
    return True

def solution(n, adj):
    # --3. adj: 가중치 기준으로 오름차순 정렬
    adj.sort(key=lambda x: x[2])
    # --4. parent 초기화
    parent =[i for i in range(n + 1)]
    sum_val = 0
    cnt = 0
    for v, u, cost in adj:
        # --5. 간선의 수가 (노드 - 1)인 경우 MST 생성
        if cnt == n - 1:
            break
        # --6. v와 u 노드가 연결되었을 때 가중치 및 간선 수 가산
        if union(parent,v, u):
            sum_val += cost
            cnt += 1
    return sum_val
        

n, m = map(int, input().split())
adj = []
for _ in range(m):
    v, u, cost = map(int, input().split())
    adj.append((v, u, cost))
    

print(solution(n, adj))
