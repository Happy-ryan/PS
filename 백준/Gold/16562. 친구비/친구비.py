n, m, k = map(int, input().split())
A = list(map(int, input().split()))
infos = [list(map(int, input().split())) for _ in range(m)]

def solution(n, m, k, A, infos):
    
    # 그룹 + 최소(최대) 관련 => 유니온파인드
    par = [-1] * (n + 1)
    sizes = [-1] * (n + 1)
    cost = [-1] + A
    
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
        
        if sizes[x] < sizes[y]:
            x, y = y, x
        
        par[y] = x
        sizes[x] += sizes[y]
        # 그룹의 최소비용!  <- root가 최소
        cost[x] = min(cost[x], cost[y])
        
        return True
    
    for info in infos:
        v, w = info
        union(v, w)
        
    
    total_cost = 0
    
    for i in range(1, n + 1):
        if find(i) == i:
            total_cost += cost[i]
            
    if total_cost > k:
        return 'Oh no'
    
    return total_cost

print(solution(n, m, k, A, infos))