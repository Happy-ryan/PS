t = int(input())

def solution(t, n, k, infos, m, qs):
    # 친구 -> 그룹
    # 연결 파악 -> 같은 그룹인지 확인
    par = [-1] * (n + 1)
    sizes = [-1] * (n + 1)
    
    def find(x):
        if par[x] == -1:
            return x
        
        root = find(par[x])
        par[x] = root
        
        return root
    
    def union(x, y):
        x, y = find(x), find(y)
        
        if x == y:
            return False
        
        if sizes[x] < sizes[y]:
            x, y,  = y, x
            
        par[y] = x
        sizes[x] += sizes[y]
        
    
    print(f"Scenario {t}:")
    for info in infos:
        a, b = info
        union(a, b)
        
    for q in qs:
        v, w = q
        if find(v) == find(w):
            print(1)
        else:
            print(0)
            
            
for i in range(t):
    n = int(input())
    k = int(input())
    infos = [list(map(int, input().split())) for _ in range(k)]
    m = int(input())
    qs = [list(map(int, input().split())) for _ in range(m)]
    solution(i +1, n, k, infos, m, qs)
    print()