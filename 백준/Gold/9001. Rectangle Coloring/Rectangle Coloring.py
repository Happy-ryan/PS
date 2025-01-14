from itertools import combinations

t = int(input())

def solution(n, rs):
    
    par = [-1] * (n + 1)
    
    
    def find(x):
        if par[x] == -1: # 부모야!
            return x
        par[x] = find(par[x]) # 부모 아니면 부모 찾아
        return par[x] # x의 root가 return 값
    
    def union(x, y):
        x = find(x) # root 찾기
        y = find(y) # root 찾기
        if x == y: # 같은 소속이면 결합안해
            return False # 결합 실패
        par[y] = x # 다른 소속이면 한 노드를 다른 소속으로 넣기
        return True # 결합 성공
    
    
    # 겹치는 것 찾기 vs 안겹치는 것 찾기
    def check_rs_1(rs1, rs2):
        flag = False
        sx_1, sy_1, lx_1, ly_1 = rs1
        sx_2, sy_2, lx_2, ly_2 = rs2
        for x in range(sx_1, lx_1 + 1):
            for y in range(sy_1, ly_1 + 1):
                if sx_2 <= x <= lx_2 and sy_2 <= y <= ly_2:
                    flag = True
        raise flag
    
    def cross(la, ra, lb, rb):
        if ra < lb or rb < la:
            return False
        return True
    
    # 겹치는 것 찾기 vs 안겹치는 것 찾기
    def check_rs_2(rs1, rs2):
        bl_xa, bl_ya, tr_xa, tr_ya = rs1
        bl_xb, bl_yb, tr_xb, tr_yb = rs2 
        if cross(bl_xa, tr_xa, bl_xb, tr_xb) and cross(bl_ya, tr_ya, bl_yb, tr_yb):
                return True
        return False
    
    res = []
    for idx1, idx2 in combinations(range(n), 2):
        if check_rs_2(rs[idx1], rs[idx2]):
            res.append((idx1 + 1, idx2 + 1))
            
    for r1, r2 in res:
        union(r1, r2)
        
    return par[1:].count(-1)
    
    
for _ in range(t):
    n = int(input())
    rs = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, rs))