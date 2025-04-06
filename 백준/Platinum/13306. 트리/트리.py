n, q = map(int, input().split())
par_node = [0, 1] + [int(input()) for _ in range(n - 1)]
qs = [list(map(int, input().split())) for _ in range(n - 1 + q)]

def solution(n, q, par_node, qs):
    # x b : x = 0, b의 부모정점과 b를 연결하는 엣지 제거
    # x c d : x = 1, c와 d가 연결이 되어있는가?
    
    par = [-1] * (n + 1)
    
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
        
        par[y] = x
        
        return True
    
    ans = []
    for q in qs[::-1]:
        if q[0] == 0:
            b = q[1]
            par_b = par_node[b]
            union(b, par_b)
        else:
            _, c, d = q
            if find(c) == find(d):
                ans.append('YES')
            else:
                ans.append('NO')
                
    for x in ans[::-1]:
        print(x)
        
solution(n, q, par_node, qs)