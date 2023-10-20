# https://www.acmicpc.net/problem/4386
import math

# --1. 대표노트 찾기
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
    parent[pa] = pb
    return True

# --3. 비용 구하는 함수
def cost(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dist = round(dist, 2)
    return dist


def solution(n, adj):
    # --4. adj: 가중치 기준으로 오름차순 정렬
    adj.sort(key=lambda x:x[2])
    # --5. parent 초기화
    parent =[i for i in range(n + 1)]
    sum_val = 0
    cnt = 0
    for v, u, cost in adj:
        # --6. 간선의 수가 (노드 - 1)인 경우 MST 생성
        if cnt == n - 1:
            break
        # --7. v와 u노드가 연결되었을 때 가중치 및 간선 수 가산
        if union(parent, v, u):
            sum_val += cost
            cnt += 1
    return sum_val
            

n = int(input())
coordinates = [list(map(float, input().split())) for _ in range(n)]
adj = [] 
for v in range(n):
    for u in range(v + 1, n):
        x1, y1 = coordinates[v]
        x2, y2 = coordinates[u]
        adj.append((v, u, cost(x1, y1, x2, y2)))
        
print(solution(n, adj))