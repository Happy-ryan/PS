# https://www.acmicpc.net/problem/1647
# 무방향성 그래프, 임의의 집끼리 모두 연결 존재, 비용의 최소 => 최소 스패닝 트리

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def solution(n, m, edges):
    
    # par / size
    par = [-1] * (n + 1)
    sizes = [1] * (n + 1)
    
    # find
    def find(x):
        if par[x] == -1:
            return x
        root = find(par[x])
        par[x] = root
        return root
    
    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        # if sizes[x] < sizes[y]:
        #     x, y = y, x
        par[y] = x
        sizes[x] += sizes[y]
        return True
        
    edges.sort(key=lambda x : x[2]) # 비용 정렬
    
    cnt = n # 처음 부모의 수
    cost = 0
    for a, b, c in edges:
        if cnt == 2:
            return cost
        if union(a, b):
            cost += c
            cnt -= 1
            
    # 2그룹으로 끝내 나누지 못할 때!
    return -1

print(solution(n, m, edges))