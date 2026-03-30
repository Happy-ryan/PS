T = int(input())

def solution(F, friends):
    
    idx = 1
    check = {}
    for friend in friends:
        # print(friend)
        f1, f2 = friend
        if f1 not in check:
            check[f1] = idx
            idx += 1
        if f2 not in check:
            check[f2] = idx
            idx += 1
    
    par = [-1 for _ in range(len(check.keys()) + 1)]
    sizes = [1 for _ in range(len(check.keys()) + 1)]
    
    def find(x):
        if par[x] == -1:
            return x
        
        par[x] = find(par[x])
        return par[x]
    
    def union(x, y):
        x, y = find(x), find(y)
        
        if x == y:
            return False
        
        if y > x : x, y = y, x
        
        par[y] = x # 큰 놈이 부모
        sizes[x] += sizes[y]
        return True

    
    for friend in friends:
        p1 = check[friend[0]]
        p2 = check[friend[1]]
        union(p1, p2)
        # print(par)
        # print(sizes)
        print(sizes[find(p1)])

for _ in range(T):
    F = int(input())
    friends = [list(input().split()) for _ in range(F)]
    solution(F, friends)