h, w = map(int, input().split())
heights = list(map(int, input().split()))

from copy import deepcopy

def solution(h, w, heights):
    board = [[0 for _ in range(w)] for _ in range(h)] # 0 빈칸
    
    for idx, height in enumerate(heights):
        for i in range(h - 1, h - height - 1, -1):
            board[i][idx] = 1 # 1 블록
    
    # 시간복잡도(W * H)
    def rain():
        for j in range(len(board[0])):
            for i in range(len(board) - 1, -1, -1):
                if board[i][j] == 0:
                    board[i][j] = 2
                    break # 비어있는 첫 번째 칸만 보면 된다!
    # 하, 좌, 우
    dr = [1, 0, 0]
    dc = [0, -1, 1]
    def in_range(r, c):
        return 0 <= r < h and 0 <= c < w
    
    # 시간복잡도(W * H * 3 * 2)
    def check_water():
        # -> 방향 물 제거
        # 시간복잡도(W * H * 3)
        for j in range(len(board[0])):
            for i in range(len(board) - 1, -1, -1):
                cnt = 0
                if i == len(board) - 1:
                    cnt += 1
                if board[i][j] == 2:
                    for k in range(3):
                        nr = i + dr[k]
                        nc = j + dc[k]
                        if in_range(nr, nc) and board[nr][nc] != 0:
                            cnt += 1
                    if cnt < 3:
                        board[i][j] = 0
                        continue
        # <- 방향 물 제거            
        for j in range(len(board[0]) -1, -1, -1):
            for i in range(len(board) - 1, -1, -1):
                cnt = 0
                if i == len(board) - 1:
                    cnt += 1
                if board[i][j] == 2:
                    for k in range(3):
                        nr = i + dr[k]
                        nc = j + dc[k]
                        if in_range(nr, nc) and board[nr][nc] != 0:
                            cnt += 1
                    if cnt < 3:
                        board[i][j] = 0
                        continue
    # 시간복잡도(W * H)
    def is_same(b1, b2):
        for r in range(len(b1)):
            for c in range(len(b1[0])):
                if b1[r][c] != b2[r][c]:
                    return False
        return True
    
    ans = 0
    while True:
        before_board = [item[:] for item in board]
        rain()
        check_water()
        after_board = [item[:] for item in board]
        if is_same(before_board, after_board):
            for row in after_board:
                for x in row:
                    if x == 2:
                        ans += 1
            return ans
        
print(solution(h, w, heights))