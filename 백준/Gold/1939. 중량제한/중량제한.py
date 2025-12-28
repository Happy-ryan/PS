N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
X, Y = map(int, input().split())

def solution1(N, M, edges, X, Y):
    
    edges.sort(key=lambda x : -x[2])
    
    inf = int(1e10)
    par = [-1] * (N + 1)
    weights = [inf] * (N + 1)
    
    def find(x):
        if par[x] == -1:
            return x    
        
        root = find(par[x])
        par[x] = root
        return root
    
    def union(x, y, w):
        x, y = find(x), find(y)
        
        if x == y:
            return False
        
        par[y] = x
        weights[x] = min(weights[x], w)
        
        return True
    
    for edge in edges:
        A, B, W = edge
        # print(f"A: {A}, B: {B}, W: {W}")
        # print(f"결합전, par: {par[1:]} / weights: {weights[1:]}")
        union(A, B, W)
        # print(f"결합후, par: {par[1:]} / weights: {weights[1:]}")
        # print("-")
        
        # W를 정렬해놔서 A, B가 연결되면 더 이상 합칠 필요 없음.
        # A, B 연결되면 그 이후는 더 이상 금지.
        if find(X) == find(Y):
            # print("끝 by 임짱")
            break
        
    # print("루트",find(X), find(Y))
    # print(par)
    # print(weights)
    
    return weights[find(A)]
    
print(solution1(N, M, edges, X, Y))