# 1. 먹을 수 있는 물고기가 없다면 -> 엄마상어게게 요청
# 2. 먹을 수 있는 물고기 1마리 -> 먹음
# 3. 먹을 수 있는 물고기 1마리 초과 -> 거리 가장 가까운 물고기

# 거리 = 아기상어 -> 물고기까지의 최단거리
# 거리 동일 물고기 -> 1순위-위 / 2순위 -왼쪽

# 이동 시간 1초
# 물고기 섭취 시 빈칸 -> 섭취하면 크기 증가

# 엄마상어한테 요청하지 않고 잡아먹을 수 있는 시간

# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

def solution(n, board):
    
    inf = int(1e18)
    
    shark = 2
    # 물고기까지의 최단거리 파악 - bfs
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n
    
    def find_closest_fish(r, c):
        
        # 방문한 곳 재방문 가능
        in_queue = [[False for _ in range(n)] for _ in range(n)]
        dist = [[inf for _ in range(n)] for _ in range(n)]
        
        dq = deque([])
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
                    shark >= board[nr][nc]:
                    dq.append((nr, nc))
                    in_queue[nr][nc] = True
                    dist[nr][nc] = dist[cr][cc] + 1     
                    
        fishes = []
        for i in range(n):
            for j in range(n):
                # 물고기의 크기는 1 ~ 6이다..
                if 0 < board[i][j] and board[i][j] <= 6 and board[i][j] < shark:
                    fishes.append((dist[i][j], i, j))

        # 거리 (dist 작을수록) -> 위에 (i 작을수록) -> 왼쪽에 (j 작을수록) -> 전부 오름차순
        fishes.sort(key=lambda x : (x[0], x[1], x[2]))
    
        return fishes
    
    def eat_fish(fishes):
        # dist >= inf 도달 불가!!
        for fish in fishes:
            dist, i, j = fish
            if dist < inf:
                board[i][j] = 9
                return dist, i, j
        # 먹을 수 있는 물고기가 없다는 뜻!
        return inf, inf, inf
    
    def find_shark():
        # 물고기의 크기가 10이 되면 상어 자기자신도 물고기 후보에 포함
        # 따라서 자기 자신을 먹어서 board 상에 '9'가 존재하지 않음.
        for i in range(n):
            for j in range(n):
                if board[i][j] == 9:
                    return (i, j)
                
    time = 0
    cnt = 0
    while True:
        s_i, s_j = find_shark()
        fishes = find_closest_fish(s_i, s_j)
        # 후보 물고기 없음
        if not fishes:
            break
        # 후보 물고기가 있는데 도달불가능
        dist, i, j = eat_fish(fishes)
        if dist == inf:
            break
        time += dist
        board[s_i][s_j] = 0
        cnt += 1
        # 크기만큼 먹으면 상어 크기 +1 / 먹은양 초기화
        if shark == cnt:
            shark += 1
            cnt = 0
    
    return time

print(solution(n, board))   