n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

def solution(n, m, board):
    # 치즈 구멍 / 치즈 가장자리 구분 -> 가장자리가 녹음
    # bfs를 통해 치즈 구멍인지 그냥 비어있는 곳인지 판단 > 다른 그룹에 속함
    # (0, 0) & bfs > 전부 그냥 비어있는 곳 > 근접 치즈 녹이기
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def bfs(r, c, mode):
        
        if mode == 'c':
            H = 1
        else:
            H = 0
        
        queue = [[False for _ in range(m)] for _ in range(n)]
        
        dq = deque([])
        
        dq.append((r, c))
        queue[r][c] = True
        grids = [(r, c)]
        
        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if  in_range(nr, nc) and\
                    board[nr][nc] == H and\
                    not queue[nr][nc]:
                        
                        dq.append((nr, nc))
                        queue[nr][nc] = True
                        grids.append((nr, nc))
                        
        return grids
    
    # 치즈를 동시에 녹여야함. 하나씩이 아니라.
    def melt_effect(airs):
        
        melts = set() # 치즈 좌표 중복 제거
        
        for air in airs:
            r, c = air
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if in_range(nr, nc) and\
                    board[nr][nc] == 1:
                        melts.add((nr, nc))
        
        for melt in melts:
            r, c = melt
            board[r][c] = 0
        
        return len(melts) # 녹는 치즈의 수
    
    t = 0
    while True:
        airs = bfs(0, 0, 'a')
        if len(airs) == n * m:
            return f"{t}\n{melts}"
        t += 1
        melts = melt_effect(airs)
        # print(f"시간: {t}, 녹는 치즈의 수: {melts}")
        
print(solution(n, m, board))