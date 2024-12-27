# https://www.acmicpc.net/problem/24542

n, m = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(m)]

def solution(n, m, friends):
    mod = int(1e9) + 7
    
    par = [-1] * (n + 1)
    size = [1] * (n + 1)
    
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
        if size[x] < size[y]:
            x, y = y, x
        par[y] = x
        size[x] += size[y]
        
    for friend in friends:
        x, y = friend
        union(x, y)
        
    sum_val = 1
    
    for idx in range(1, n + 1):
        if par[idx] == -1:
            sum_val *= size[idx]
            sum_val %= mod
    
    return sum_val
            

print(solution(n, m, friends))