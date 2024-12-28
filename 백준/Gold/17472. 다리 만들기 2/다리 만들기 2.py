N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

from collections import deque
from itertools import combinations

def solution(N, M, board):
    # 섬을 구하는 알고리즘 - bfs
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    in_queue = [[False for _ in range(M)] for _ in range(N)]
    
    def in_range(r, c):
        return 0 <= r < N and 0 <= c < M
    
    def bfs(r, c):
        group = []
        dq = deque([])
        
        dq.append((r, c))
        group.append((r, c))
        in_queue[r][c] = True
        
        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and not in_queue[nr][nc] and board[nr][nc] == 1:
                    dq.append((nr, nc))
                    in_queue[nr][nc] = True
                    group.append((nr, nc))
                    
        return group
    
    # 섬의 집합 <- bfs을 통해서 
    dic = {}
    groups = []
    for i in range(N):
        for j in range(M):
            if in_queue[i][j] or board[i][j] == 0:
                continue
            groups.append(bfs(i, j))
        
    # 섬의 개수 = 노드의 수
    island_cnt = len(groups)
    
    for idx in range(island_cnt):
        dic[idx + 1] = groups[idx]

    # 섬끼리의 다리의 최소 다리의 길이
    inf = int(1e18)
    def cal_min_dis(island1, island2):
        island1_gird = dic[island1]
        island2_gird = dic[island2]
        # 목표
        dis = inf
        for r1, c1 in island1_gird:
            for r2, c2 in island2_gird:
                if r1 == r2 and c1 != c2:
                    l, r = min(c1, c2), max(c1, c2)
                    # 점-점 = 다리의 길이
                    cnt = 0
                    for c in range(l + 1, r):
                        if board[r1][c] == 1:
                            cnt = 0
                            break
                        else:
                            cnt += 1
                    if cnt >= 2:
                        dis = min(cnt, dis)
                elif r1 != r2 and c1 == c2:
                    l, r = min(r1, r2), max(r1, r2)
                    cnt = 0
                    for r in range(l + 1, r):
                        if board[r][c1] == 1:
                            cnt = 0
                            break
                        else:
                            cnt += 1
                    if cnt >= 2:
                        dis = min(cnt, dis)
        return dis
    
    # 각 섬을 2개씩 뽑아서 최소 다리의 길이 구함.
    edges = []
    for row in combinations(range(1, island_cnt + 1), 2):
        is1, is2 = row
        dis = cal_min_dis(is1, is2)
        edges.append((is1, is2, dis))
    # print(edges)
    # 각 섬은 하나의 노드로 보고 MST 진행!
    par = [-1] * (island_cnt + 1) # 1base
    sizes = [1] * (island_cnt + 1)
    
    def find(x):
        # -1이면 부모다!
        if par[x] == -1:
            return x
        # 부모의 부모를 찾는다..
        root = find(par[x])
        # root가 내 부모다!하고 붙인다!
        par[x] = root
        return root
    
    def union(x, y):
        x = find(x)
        y = find(y)
        # 부모가 같다는 것이니 결합할 필요 없음!
        if x == y:
            return False
        # if sizes[x] < sizes[y]:
        #     x, y = y, x
        par[y] = x
        sizes[x] += sizes[y]
        return True
    # 비용기준으로 정렬
    edges.sort(key=lambda x : x[2])
    
    cost = 0
    for is1, is2, dis in edges:
        if union(is1, is2):
            cost += dis
        
    # print(par)
    # print(sizes)
    # print(cost)
    if cost >= inf:
        return -1
    return cost


print(solution(N, M, board))