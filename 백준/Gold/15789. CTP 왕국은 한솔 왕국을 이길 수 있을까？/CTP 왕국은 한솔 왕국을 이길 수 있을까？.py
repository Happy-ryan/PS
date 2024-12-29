# https://www.acmicpc.net/problem/15789

N, M = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(M)]
C, H, K = map(int, input().split())

def solution(N, M, infos, C, H, K):
    
    par = [-1] * (N + 1)
    sizes = [1] * (N + 1)
    
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
        # if sizes[x] < sizes[y]:
        #     x, y = y, x
        par[y] = x
        sizes[x] += sizes[y]
        return True
    
    # union의 결과 -> CTP 그룹 / H그룹 / 그외 그룹들
    for a, b in infos:
        union(a, b)
        
    # CTP root와 한솔 root
    CTP_root = find(C)
    H_root = find(H)
    # 위 둘을 제외한 부모노드들
    root_nodes = []
    for idx, root in enumerate(par[1:]):
        if root == -1:
            root_nodes.append(idx + 1)
            
    root_nodes.remove(CTP_root)
    root_nodes.remove(H_root)
    
    # print(root_nodes)
    
    candidates = []
    for root in root_nodes:
        candidates.append(sizes[root])
    
    candidates.sort(reverse=True)
    # print(candidates)
    
    # 기존 CTP 왕국의 힘 + 새로운 동맹 후보군의 힘 = CTP왕국의 최종 힘
    return sizes[CTP_root] + sum(candidates[:min(K, len(candidates) + 1)]) 
    
print(solution(N, M, infos, C, H, K))