import sys
input = sys.stdin.readline

def solution(N, circles):
    par = [-1] * N
    
    def find(x):
        if par[x] == -1:
            return x
        par[x] = find(par[x])
        return par[x]
    
    def union(x, y):
        x, y = find(x), find(y)
        if x == y:
            return False
        if x > y:
            x, y = y, x
        par[y] = x
        return True
    
    for i in range(N):
        x1, y1, r1 = circles[i]
        for j in range(i + 1, N):
            x2, y2, r2 = circles[j]
            
            dist_sq = (x1 - x2)**2 + (y1 - y2)**2
            if dist_sq <= (r1 + r2)**2:
                union(i, j)
    
    return len(set(find(i) for i in range(N)))

T = int(input())
for _ in range(T):
    N = int(input())
    circles = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, circles))