n, m, t = map(int, input().split())
k, a, b = map(int, input().split())
board = [list(input()) for _ in range(n)]

def solution(n, m, t, k, a, b, board):
    # 1 / 0
    for r in range(n):
        for c in range(m):
            if board[r][c] == '*':
                board[r][c] = 1
            else:
                board[r][c] = 0
    # 주변의 생명의 개수를 세는 방법에 대한 고민 필요
    # 이중포문 쓰면 시간복잡도 O(MAX(N, M)^2) = O(100*100) => 이 부분을 줄여야함.
    # 각 생명 찾는 방법 - O(N * M) = O(100 * 100) => 무조건 해야함
    # 생명 찾기 & 주변 체크 = O(N * M * MAX(N, M) * MAX(N, M)) => 시간초과
    def get_grid(r, c):
        l_r = max(0, r - k)
        l_c = max(0, c - k)
        r_r = min(n - 1, r + k)
        r_c = min(m - 1, c + k)
        grids = []
        for i in range(l_r, r_r + 1):
            for j in range(l_c, r_c + 1):
                if i == r and j == c:
                    continue
                grids.append((i, j))
        grids.sort(key=lambda x : (x[0], x[1]))
        return grids
        
    def build_psum():
        psum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for r in range(1, n + 1):
            for c in range(1, m + 1):
                psum[r][c] = board[r - 1][c - 1] + psum[r - 1][c] + psum[r][c - 1] - psum[r - 1][c - 1]
        
        return psum
                
    def get_life(r, c, psum):
        l_r = max(0, r - k)
        l_c = max(0, c - k)
        r_r = min(n - 1, r + k)
        r_c = min(m - 1, c + k)
        # psum[bottom_r][bottom_c] - psum[left_r][bottom_c] - psum[bottom_r][left_c] + psum[left_r][left_c]
        val = psum[r_r + 1][r_c + 1] - psum[l_r][r_c + 1] - psum[r_r + 1][l_c] + psum[l_r][l_c]
        
        if board[r][c] == 1:
            val -= 1
            
        return val
    
    
    def state_check(r, c, psum):

        life_cnt = get_life(r, c, psum)

        if board[r][c] == 1 and a <= life_cnt and life_cnt <= b:
            return 0 # 생존(*)
        elif board[r][c] == 1 and life_cnt < a:
            return 1 # 고독('')
        elif board[r][c] == 1 and b < life_cnt:
            return 2 # 과밀('')
        elif board[r][c] != 1 and a < life_cnt and life_cnt <= b:
            return 3 # 탄생(*)
        
    def one_time():
        psum = build_psum()
        states = []
        for cr in range(n):
            for cc in range(m):
                state = state_check(cr, cc, psum)
                if state == 0 or state == 3:
                    states.append((cr, cc, 1))
                elif state == 1 or state == 2:
                    states.append((cr, cc, 0))
        
        for st in states:
            cr, cc, sta = st
            board[cr][cc] = sta
                

    for time in range(t):
        # print(f"time: {time + 1}")
        one_time()
        # for row in board:
        #     print(*row)
        # print("=" * 10)
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                print('*', end = '')
            else:
                print('.', end = '')
        print()
        
solution(n, m, t, k, a, b, board)