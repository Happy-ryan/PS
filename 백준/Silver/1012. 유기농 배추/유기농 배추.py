# https://www.acmicpc.net/problem/1012
from collections import deque

def bfs(row, col, board):
    in_queue = [[False for col in range(col)] for row in range(row)]
    
    def check(r, c):
        return 0<= r < row and 0<= c <col and not in_queue[r][c] and\
            board[r][c] == 1 
            
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    q = deque([])
    cnts = [] # 연결된 part들이 몇 개의 블록으로 이루어져 있는지 알 수 있는 곳
    cnt = 0
    for r in range(row):
        for c in range(col):
            if not check(r, c):
                continue
            q.append((r, c))
            in_queue[r][c] = True
            cnt = 0
            while q:
                cnt += 1 # 연결된 것 모두 찾아냄
                cr, cc = q.popleft()
                for k in range(4):
                    nr = cr + dr[k]
                    nc = cc + dc[k]
                    if check(nr, nc):
                        in_queue[nr][nc] = True
                        q.append((nr, nc))
            cnts.append(cnt)
                        
    return len(cnts)

def solution(row, col, board):
    return bfs(row, col, board)


t = int(input())

for _ in range(t):
    col, row, case = map(int, input().split())
    board = [[0 for _ in range(col)] for _ in range(row)]
    for _ in range(case):
        c_, r_ = map(int, input().split()) # 열, 행
        board[r_][c_] = 1
    print(solution(row, col, board))
