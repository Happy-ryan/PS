'''
4 : 게이트 수
3 : 비행기 수
4 : 첫 번째 비행기는 1 ~ 4번째 게이트에 도킹 가능
1 : 두 번째 비행기는 1 ~ 1번째 게이트에 도킹 가능
1 : 세 번째 비행기는 1 ~ 1번째 게이트에 도킹 가능

> 
'''

def solution(G, P, planes):
    par = [-1 for _ in range(G + 1)]
    
    def find(x):
        if par[x] == -1:
            return x
        par[x] = find(par[x])
        return par[x]
    
    def union(x, y):
        x = find(x)
        y = find(y)
        
        if x == y:
            return
        
        # 핵심: 큰 번호가 작은 번호를 가리키도록
        if x > y:
            x, y = y, x
        
        par[y] = x
    
    count = 0
    
    for gi in planes:
        available = find(gi)
        
        if available == 0:
            break
        # gi번 게이트에 도킹하고, gi와 gi-1을 합침
        union(gi, available - 1)
        count += 1
    
    return count

G = int(input())
P = int(input())
planes = [int(input()) for _ in range(P)]
print(solution(G, P, planes))