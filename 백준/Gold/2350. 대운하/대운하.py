n, m, k = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
qs = [list(map(int, input().split())) for _ in range(k)]

def solution(n, m, k, edges, qs):
    # 각 도시 간 연결 > 그룹핑 + 최대(최소) 비용(거리) 등 찾기 -> 다익스트라 or 유니온파인드로 접근
    
    # union find 공식
    par = [-1] * (n + 1)
    sizes = [-1] * (n + 1)
    
    # root를 찾는 함수
    def find(x):
        # 내가 지금 넣은 지점이 root인가?
        if par[x] == -1: # 그렇다!
            return x
        
        root = find(par[x])
        par[x] = root
        
        return root
    
    def union(x, y):
        x = find(x) # 각각의 부모를 찾음
        y = find(y)
        
        # 같은 가족인지 확인 -> 가족이면 결합 no
        if x == y:
            return False
        # 최적화 x가 항상 사이즈가 크도록
        if sizes[x] < sizes[y]:
            x, y = y, x
            
        # y가 x에게 가서 붙기
        par[y] = x
        sizes[x] += sizes[y]
        
        return True
    
    # 최소 운하의 폭 = 최대 배의 폭
    # 운하 폭(w) 기준
    from collections import defaultdict
    
    dic = defaultdict(list)
    check = [0] * len(qs)
    for i, j, w in edges:
        dic[w].append((i, j))
    
    # 폭이 큰 노선부터 연결하기
    for w in range(200, 0, -1):
        # 해당 폭이 건설 계획 중!
        if w in dic:
            egs = dic[w]
            # 두 도시 연결
            for i, j in egs:
                union(i, j)
        # 연결 이후에 배가 지나갈 수 있는 배의 최대 폭 기록!!
        
        # find(s) == find(e) : 같은 그룹 -> 즉, 운하로 연결되어 이동가능하다는 의미! 
        # 0 인것을 확인하는 이유 : 폭이 큰거부터 확인하기 때문에 이미 들어가 있다는건 이전에 최대 폭이 들어옴!
        for idx, q in enumerate(qs):
            s, e = q
            if find(s) == find(e) and check[idx] == 0:
                check[idx] = w
    
    for c in check:
        print(c)
        
    
solution(n, m, k, edges, qs)