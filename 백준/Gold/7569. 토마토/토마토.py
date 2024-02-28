m, n, h = map(int, input().split())
# 입력 - (열, 행, 높이)
# 인덱스 - [높이][행][열]
boards = [
        [list(map(int, input().split())) for _ in range(n)]
            for _ in range(h)
            ]

from collections import deque
# 위아래가 추가된다!
dirs = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1),
        (1, 0, 0), (-1, 0, 0)]

def solution(n, m, h, boards):
    # 출발점이 많은 bfs + 3차원
    # 열 > 행 > 높이
    in_queue = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
    # 한 번에 전부 바뀌므로 day를 기록해야함! < 이 문제의 포인트!
    inf = int(1e9)
    days = [[[-inf for _ in range(m)] for _ in range(n)] for _ in range(h)]
        
    def in_range(k, r, c):
        return 0 <= r < n and 0 <= c < m and 0 <= k < h
    
    def find_end_tomatos():
        # 시간복잡도 N(100^3) 
        end_tomatos = []
        for k in range(h):
            for i in range(n):
                for j in range(m):
                    if boards[k][i][j] == 1:
                        end_tomatos.append((k, i, j))
                        
        return end_tomatos
    
    def bfs():
        dq = deque([])
        
        for end_tomato in find_end_tomatos():
            k, i, j = end_tomato
            dq.append((k, i, j))
            in_queue[k][i][j] = True
            days[k][i][j] = 0
        
        go_tomatos = []
        while dq:
            ck, cr, cc = dq.popleft()
            for k in range(6):
                nk = ck + dirs[k][0]
                nr = cr + dirs[k][1]
                nc = cc + dirs[k][2]
                if in_range(nk, nr, nc) and not in_queue[nk][nr][nc] and boards[nk][nr][nc] == 0:
                    dq.append((nk, nr, nc))
                    in_queue[nk][nr][nc] = True
                    days[nk][nr][nc] = max(days[ck][cr][cc] + 1, days[nk][nr][nc])
                    
                    boards[nk][nr][nc] = 1
                    
                    
    bfs()
    
    # 불가능상황 - 토마토(0) & days(-inf)인 경우는 불가능한 경우이다.
    max_days = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if boards[k][i][j] == 0 and days[k][i][j] <= -inf:
                    return -1
                max_days = max(max_days, days[k][i][j])
    
    return max_days

print(solution(n, m, h, boards))