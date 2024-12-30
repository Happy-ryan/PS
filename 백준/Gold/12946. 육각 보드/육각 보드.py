n = int(input())
board = [list(input()) for _ in range(n)]

from collections import deque, Counter

def solution(n, board):
    # 필요한 색의 '최소' 종류 > bfs 고려!!
    # 접하는 곳은 같은 색으로 칠할 수 없다! <- 주의
    
    # 6각보드이므로 이동방향 최대 6가지
    dr = [-1, -1, 0, 1, 1, 0]
    dc = [0, 1, 1, 0, -1, -1]
    
    # 7색(1 ~ 7) + 방문하지않음(-1).
    in_queue = [[-1 for _ in range(n)] for _ in range(n)]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n
    
    
    def get_color(r, c):
        ex_color = []
        for d in range(6):
            nr = r + dr[d]
            nc = c + dc[d]
            if in_range(nr, nc) and in_queue[nr][nc] != -1:
                ex_color.append(in_queue[nr][nc])
        
        for color in range(1, 8):
            if color not in ex_color:
                return color
    
    
    def bfs(r, c):
        dq = deque([])
        
        dq.append((r, c))
        in_queue[r][c] = 1
        
        while dq:
            cr, cc = dq.popleft()
            for d in range(6):
                nr = cr + dr[d]
                nc = cc + dc[d]
                if in_range(nr, nc) and\
                    in_queue[nr][nc] == -1 and\
                    board[nr][nc] == 'X':
                    dq.append((nr, nc))
                    in_queue[nr][nc] = get_color(nr, nc)
                    
                    
    for i in range(n):
        for j in range(n):
            if in_queue[i][j] != -1 or board[i][j] == '-':
                continue
            bfs(i, j)
    
    
    dic = Counter()
    for i in range(n):
        for j in range(n):
            dic[in_queue[i][j]] += 1
            
    if -1 in dic:
        dic.pop(-1)
    
    return min(3, len(dic))

print(solution(n, board))