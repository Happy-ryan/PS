T = int(input())

def solution(N, edges):
    
    dic = {}
    num = 1
    for i in range(N):
        a, b = edges[i]
        if a not in dic:
            dic[a] = num
            num += 1
        if b not in dic:
            dic[b] = num
            num += 1
    
    # print(dic)
    k = len(dic)
    par = [-1] * (k + 1)
    sizes = [1] * (k + 1)
        
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
            x, y = y, x
        
        par[y] = x
        sizes[x] += sizes[y]
        
        return True
    
    for edge in edges:
        x, y = dic[edge[0]], dic[edge[1]]
        union(x, y)
        
        par_x = find(x)
        
        # print(f"par: {par}")
        # print(f"sizes : {sizes}")
        # print(f"정답 : {sizes[par_x]}")
        print(sizes[par_x])
        
for _ in range(T):
    N = int(input())
    edges = [list(input().split()) for _ in range(N)]
    solution(N, edges)