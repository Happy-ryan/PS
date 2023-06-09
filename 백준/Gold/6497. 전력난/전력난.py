# https://www.acmicpc.net/problem/6497
# MST인 근거: 절약할 수 있는 최대 비용 > 최소비용으로 연결 & 그래프 > MST
import sys
sys.setrecursionlimit(10**4)

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
    parent[pa]=pb
    return True
        
        
def solution(n, adj):
    # --2. adj 가중치 기준으로 오름차순 정렬
    adj.sort(key=lambda x: x[2])
    # -- 간선의 총합
    total_cost = sum([row[2] for row in adj])
    # --4. parent 초기화(집번호 0번부터 존재함)
    parent =[i for i in range(n)]
    sum_val = 0
    cnt = 0
    for u, v, cost in adj:
        # --5. 간선의 수가 (노드 - 1)인 경우 MST 생성
        if cnt == n - 1:
            break
        # --6. v와 u 노드가 연결되었을 때 가중치 및 간선 수 가산
        if union(parent,u, v):
            sum_val += cost
            cnt += 1
    return abs(sum_val - total_cost)
        
        
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    adj = []
    for i in range(m):
        u, v, cost = map(int, input().split())
        adj.append((u, v, cost))
    print(solution(n, adj))

