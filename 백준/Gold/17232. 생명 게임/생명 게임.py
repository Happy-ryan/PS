n, m, t = map(int, input().split())
k, a, b = map(int, input().split())
board = [list(input()) for _ in range(n)]

def solution(n, m, t, k, a, b, board):
    
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
        
    def state_check(r, c):
        adj_grids = get_grid(r, c)
        life_cnt = 0
        for grid in adj_grids:
            i, j = grid
            if board[i][j] == '*':
                life_cnt += 1
        if board[r][c] == '*' and a <= life_cnt and life_cnt <= b:
            return 0 # 생존(*)
        elif board[r][c] == '*' and life_cnt < a:
            return 1 # 고독('')
        elif board[r][c] == '*' and b < life_cnt:
            return 2 # 과밀('')
        elif board[r][c] != '*' and a < life_cnt and life_cnt <= b:
            return 3 # 탄생(*)
        
    def one_time():
        
        states = []
        for cr in range(n):
            for cc in range(m):
                state = state_check(cr, cc)
                if state == 0 or state == 3:
                    states.append((cr, cc, '*'))
                elif state == 1 or state == 2:
                    states.append((cr, cc, '.'))
        
        for st in states:
            cr, cc, sta = st
            board[cr][cc] = sta
                
        
    
    for time in range(t):
        # print(f"time: {time + 1}")
        one_time()
        # for row in board:
        #     print(*row)
        # print("=" * 10)
    
    for row in board:
        print(''.join(row))
        
solution(n, m, t, k, a, b, board)