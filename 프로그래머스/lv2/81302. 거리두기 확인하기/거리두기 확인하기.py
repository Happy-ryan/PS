# bfs
from collections import deque

def find(places):
    p = []
    for r in range(5):
        for c in range(5):
            if places[r][c] == 'P':
                p.append((r, c))
    return p

def solution(places):
    answer = []
    inf = int(1e18)
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def bfs(places, sr, sc):
        flag = True
        in_queue = [[False for col in range(5)] for row in range(5)]
        dist =[[inf for col in range(5)] for row in range(5)]
        
        def check(r, c):
            return 0 <= r < 5 and 0 <= c < 5 and not in_queue[r][c] and places[r][c] != 'X'
        
        q = deque([])
        q.append((sr, sc))
        in_queue[sr][sc] = True
        dist[sr][sc] = 0
        
        while q:
            cr, cc = q.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if check(nr, nc):
                    q.append((nr, nc))
                    in_queue[nr][nc] = True
                    dist[nr][nc] = dist[cr][cc] + 1
                    if places[nr][nc] == 'P' and 1 <= dist[nr][nc] <= 2:
                        flag = False
        return flag
    ans = [1, 1, 1, 1, 1] # 기본 1 로 잡은 이유 : 응시자가 없을 경우 무조건 거리두기 만족하므로 그것을 고려하기 위함
    for i, place in enumerate(places):
        for x, y in find(place):
            if bfs(place, x, y) == False:
                ans[i] = 0 
                break # P의 좌표를 돌면서 Fasle 가 나오는 순간 place 탐색 중단하고 새로운 place 탐색하기
    return ans