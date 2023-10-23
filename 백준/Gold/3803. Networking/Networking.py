# https://www.acmicpc.net/problem/3803

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

def merge(n, adj):
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

result = []
while True:
    nums = list(map(int, input().split()))
    
    if nums[0] == 0:
        break
    n, m = nums 
    adj = []
    for _ in range(m):
        v, u, cost = map(int, input().split())
        adj.append((v, u, cost))
    result.append(merge(n, adj))
    input()
    
for x in result:
    print(x)