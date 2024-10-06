import sys

input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

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
        # 양방향 물제거 하는 이유 - ->방향만 제거하면 (빈)(비1)(비2)(빈) 인 상태가 제거되지 않는다.                            (블1)(블2)(블3)    
        # 왜냐하면 -> 방향을 먼저 보니까 (비1)의 경우에는 (빈)(비2)(블1)로 둘러싸여있기 때문
        # 따라서 시작하는 방향에 따라서 물 제거가 다를 수 있으니 양방향을 보자
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
                    # 하, 좌, 우로 나를 둘러싸야 고일 수 있다.
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
        # deepcopy 쓰면 너무 느리다!!
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
        
from collections import defaultdict
def solution2(h, w, heights):
    board = [[0 for _ in range(w)] for _ in range(h + 1)] # 0 빈칸
    inf = int(1e18)
    
    min_idx = inf
    max_idx = -inf
    
    dic = defaultdict(list)
    for idx, height in enumerate(heights):
        dic[height].append(idx)
        
    for height, idx_row in sorted(dic.items(), key=lambda x: -x[0]):
        for idx in idx_row:
            min_idx = min(min_idx, idx)
            max_idx = max(max_idx, idx)
        for j in range(min_idx, max_idx + 1):
            board[height][j] = 1
    
    cnt = 0
    for j in range(len(board[0])):
        for i in range(len(board) - 1, -1, -1):
            if board[i][j]:
                cnt += i - heights[j]
                break
                
    
    return cnt
        
print(solution2(h, w, heights))