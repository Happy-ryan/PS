# https://www.acmicpc.net/problem/14621

# --1. 대표노드 찾기
# 내가 대표노드가 아니면 대표노드 찾을 때까지 재귀!
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
        return parent[x]
    return x

# --2.  대표노드끼리 연결
def union(parent, a, b):
    # 대표노드 찾기
    pa = find(parent, a)
    pb = find(parent, b)
    # 이미 연결된 상태
    if pa == pb:
        return False
    # 연결 안되어있으면 한 명이 자식으로 들어가지
    parent[pa] = pb
    return True

def solution(n, adj):
    # --3. adj: 가중치 기준으로 오름차순 정렬
    adj.sort(key=lambda x:x[4])
    # --4. parent 초기화
    parent =[i for i in range(n + 1)]
    sum_val = 0
    cnt = 0
    for gender_v, gender_u, v, u, cost in adj:
        # --5-1. 간선의 수가 (노드 - 1)인 경우 MST 생성
        if cnt == n - 1:
            break
        # --5-2. 출발지와 도착지의 성별이 달랐을 때만 그래프 연결
        if gender_v == gender_u:
            continue
        # --6. v와 u노드가 연결되었을 때 가중치 및 간선 수 가산
        if union(parent, v, u):
            sum_val += cost
            cnt += 1
            # print(f"v{v} - 의 성별{gender_v}, u{u} - 의 성별{gender_u}, 비용{cost}")
    if sum_val == 0 or cnt != n - 1:
        return -1
    return sum_val
            

n, m = map(int, input().split())
genders = [0] + list(input().split())
adj = []
for idx in range(m):
    v, u, cost = map(int, input().split())
    adj.append((genders[v], genders[u], v, u, cost))
    

print(solution(n, adj))