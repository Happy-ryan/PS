import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

from collections import defaultdict, deque

def solution2(R, C, board):
    
    def find_swan():
        swans = []
        for r in range(R):
            for c in range(C):
                if board[r][c] == "L":
                    swans.append((r, c, 's'))
        return swans
    
    swans = find_swan()
    s1, s2 = swans[0], swans[1]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def in_range(r, c):
        return 0 <= r < R and 0 <= c < C
    
    inf = int(1e18)
    
    in_queue = [[False for _ in range(C)] for _ in range(R)]
    dist = [[inf for _ in range(C)] for _ in range(R)]
    
    def bfs(waters):
        
        dq = deque([])
        for water in waters:
            r, c = water
            dq.append((r, c))
            in_queue[r][c] = True
            dist[r][c] = 0
        
        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and\
                    not in_queue[nr][nc] and\
                        board[nr][nc] == 'X':
                            
                            dq.append((nr, nc))
                            in_queue[nr][nc] = True
                            dist[nr][nc] = dist[cr][cc] + 1
        
        return waters
                            
    
    waters = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'X':
                continue
            waters.append((i, j))
    
    bfs(waters)
    
    # for row in dist:
    #     print(*row)
    dic = defaultdict(list)
    for i in range(R):
        for j in range(C):
            dic[dist[i][j]].append((i, j))
    
    max_day = max(dic.keys())
    
    def index(r, c):
        return r * C + c
    
    N = R * C
    par = [-1] * (N)
    
    def find(x):
        if par[x] == -1:
            return x
        
        root = find(par[x])
        par[x] = root
        
        return root
    
    def union(x, y):
        x, y = find(x), find(y)
        
        if x == y:
            return False
        
        par[y] = x
        return True
    
    for day in range(max_day + 1):
        for r, c in dic[day]:
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if in_range(nr, nc) and\
                    dist[nr][nc] <= day:
                        union(index(r, c), index(nr, nc))
        # print(f"day : {day}")
        # print(f"par : {par}")
        if find(index(s1[0], s1[1])) == find(index(s2[0], s2[1])):
            return day
    
print(solution2(R, C, board))