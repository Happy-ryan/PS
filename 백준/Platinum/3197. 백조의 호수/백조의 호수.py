# bfs - 출발점이 여러개인 bfs
# union find - 2차원에서의 union find

from collections import deque

def solution(R, C, board):
    
    
    # 0. 백조의 위치 찾기
    def find_swan():
        swans = []
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'L':
                    swans.append((i, j))
        return swans
    
    swans = find_swan()
    
    # 1. 물의 위치 찾기
    def find_water():
        waters = []
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'X': # 빙하 아니면 모두 물(백조 포함)
                        continue
                waters.append((i, j))
        return waters
    
    waters = find_water()
    
    # 2. BFS -> 빙하 공간 녹이기 (By 물) -> 녹는 날을 기록!
    inf = int(1e18)
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    in_queue = [[False for _ in range(C)] for _ in range(R)]
    day = [[inf for _ in range(C)] for _ in range(R)] # 얼음이 녹는 날 기록
    
    def in_range(r, c):
        return 0 <= r < R and 0 <= c < C
    
    def bfs(waters):
        
        dq = deque([])
        
        for water in waters:
            r, c = water
            dq.append((r, c))
            in_queue[r][c] = True
            day[r][c] = 0 
            
        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and\
                    not in_queue[nr][nc] and\
                        board[nr][nc] == 'X': # 'X' -> '.'로 녹여야하므로,
                            dq.append((nr, nc))
                            in_queue[nr][nc] = True
                            day[nr][nc] = day[cr][cc] + 1
    
    bfs(waters)
    
    # 3. 녹는 날 - 좌표 모아주기 > 해당 좌표들의 조합으로 그룹 생성할 것!
    from collections import defaultdict
    
    dic = defaultdict(list)
    for i in range(R):
        for j in range(C):
            dic[day[i][j]].append((i, j))
    
    # 4. 백조가 같은 물 그룹(?)에 위치하는지 판단 > union find 활용
    # 2차원 union find 
    
    # 2차원 -> 1차월 배열로 index
    def index(i, j):
        return i * C + j
    # 셋팅
    N = R * C
    par = [-1 for _ in range(N)]
    
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
    
    # 얼음이 다 녹는 날
    max_day = max(dic.keys())
    # 0일 ~ max_day까지 돌면서 주어진 day 보다 작은 경우 그룹으로 병합
    # 병합하면서 두 백조의 par가 같아지면 같은 그룹에 편입 의미 > return
    for cday in range(max_day + 1):
        for r, c in dic[cday]: # day에 녹는 좌표들
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if in_range(nr, nc) and\
                    day[nr][nc] <= cday: # day보다 작으면 다 내 그룹이 되야해!!
                        union(index(r, c), index(nr, nc))
                        
        if find(index(swans[0][0], swans[0][1])) == find(index(swans[1][0], swans[1][1])):
            return cday

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
print(solution(R, C, board))