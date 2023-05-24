# https://www.acmicpc.net/problem/2178
from collections import deque

n, m = map(int, input().split())
board = [list(input()) for row in range(n)]


def bfs(n, m, board):
    in_queue = [[False for col in range(m)] for row in range(n)]
    dist = [[0 for col in range(m)] for row in range(n)]
    
    def check(r, c):
        return 0<= r < n and 0<= c < m and\
            not in_queue[r][c] and board[r][c] == "1"
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    q = deque([])
    start = (0, 0) # 시작점 고정
    q.append(start)
    cnts = []
    cnt = 0
    dist[start[0]][start[1]] = 1
    while q:
        # cnt += 1 # start에서 연견될 1 전부 찾음 -> 문제 특성 상 전부 연결되어있으므로 1의 개수가 cnt가 된다.
        cr, cc = q.popleft()   
        in_queue[cr][cc] = True
        # dist[cr][cc] = cnt 
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if check(nr, nc):
                in_queue[nr][nc] = True
                q.append((nr, nc))
                dist[nr][nc] = dist[cr][cc] + 1
                
                
    # bfs 종료되면 cnts에 너비우선탐색값 저장하기
    cnts.append(cnt)
        
    return dist[n - 1][m - 1]


def solution(n, m, board):
    return bfs(n, m, board)
    
print(solution(n, m, board))