n = int(input())
m = int(input())
cites = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

def solution(n, cites, plan):
    
    par = [-1] * (n + 1)
    sizes = [-1] * (n + 1)
    
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
        sizes[x] += sizes[y]
        
        return True
    
    # cities는 인접행렬을 의미함.
    for i in range(n):
        for j in range(n):
            if cites[i][j] == 1:
                union(i, j)
    
    ans = set()
    for p in plan:
        # 1base -> 0base
        ans.add(find(p - 1))
        
    if len(ans) == 1:
        return 'YES'
    return 'NO'

print(solution(n, cites, plan))