# https://www.acmicpc.net/problem/1647
# 무방향성 그래프, 임의의 집끼리 모두 연결 존재, 비용의 최소 => 최소 스패닝 트리

# --대표노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
        return parent[x]
    return x
# -- 대표노드간 연결
def union(parent, a, b):
    pa = find(parent, a)
    pb = find(parent, b)
    if pa == pb:
        return False
    parent[pa] = pb
    return True

def merge(adj, n):
    #
    group_num = n
    # -- 비용으로 정렬
    adj.sort(key=lambda x: x[2])
    # -- parent 자기자신의 값으로 초기화
    parent = [i for i in range(n + 1)]
    #
    sum_val = 0
    for v, u, cost in adj[:-1]:
        # if cnt == n - 1:
        #     break
        if group_num == 2:
            break
        if union(parent, v, u):
            group_num -= 1
            sum_val += cost
            # print(f"{u}와 {v}가 {cost} 비용으로 연결되었습니다.\n현재 그룹의 수는{group_num}입니다.\n---------")
            
    return sum_val
    
    

# 마을을 분리시키기 => 대표노드가 되는 애들을 분리시켜야함!
n, m = map(int, input().split())
adj = []
for _ in range(m):
    v, u, cost = map(int, input().split())
    adj.append((v, u, cost))
    
print(merge(adj, n))

# 23 / 1 / 4 / 5/ 6/ 7 - 6개
# 23 / 46 /1/ 5/ 7 - 5개
# 123 / 46 / 5 / 7 - 4개
# 5123 / 46  / 7 - 3개
# 512346 / 7 - 2개