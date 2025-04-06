n, m, k = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
qs = [list(map(int, input().split())) for _ in range(k)]

def solution(n, m, k, edges, qs):
    
    # 운하 연결 -> 그룹핑 -> union find
    par = [-1] * (n + 1)
    sizes = [1] * (n + 1)
    # 최소 운하의 폭 = 최대 배의 폭

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

        return True
    
    from collections import defaultdict
    
    dic = defaultdict(list)
    check = [0] * len(qs)
    for i, j , w in edges:
        dic[w].append((i, j))
    
    # 큰 노선부터 연결하기
    # 큰 노선을 연결하고 qs를 돌면서 연결이 되어있으면 그때가 최대 운항 폭이 될 수 있음.
    for w in range(200, 0, -1):
        if w in dic:
            egs = dic[w]
            for i, j in egs:
                union(i, j)
        
        for idx,q in enumerate(qs):
            a, b = q
            if find(a) == find(b) and check[idx] == 0:
                check[idx] = w
                
    for c in check:
        print(c)
    
solution(n, m, k, edges, qs)