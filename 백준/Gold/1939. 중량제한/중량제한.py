n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

def solution(n, m, edges, A, B):
    
    # union find
    inf = int(1e18)
    par = [-1 for _ in range(n + 1)]
    weight = [inf for _ in range(n + 1)] # 다리 옮길 수 있는 최대 무게 중 최소 무게..
    # root 뱉어내는 함수
    def find(x):
        # x가 root -> 끝
        if par[x] == -1:
            return x
        # x 가 root 아님 -> par[x]의 root 필요
        par[x] = find(par[x])
        return par[x]
    # y -> x (root에 가깝도록) - 작은 놈이 root에 가깝도록
    def union(x, y, w):
        x, y = find(x), find(y)
        if x == y:
            return False
        
        if x > y: x, y = y, x
        par[y] = x
        weight[x] = min(weight[x], w) # 최대 중량 중 최소
        return True
        
    
    # union - 중량이 큰 것(최대)부터 결합하고 그 중 최소 
    edges.sort(key=lambda x : -x[2])
    for u, v, w in edges:
        # print(f"결합 전: {par}")
        union(u, v, w) # 결합순서가 영향을 줌..> 정렬이 필요함!!!
        # print(f"결합 후: {par}")
        # print('-')
        # 결합 완료 > 종료를 안시키면 최대 무게가 아니라 최소 무게로 갱신될 것.
        if find(A) == find(B):
            break
        
    
    return weight[find(B)]
        
    
        
print(solution(n, m, edges, A, B))