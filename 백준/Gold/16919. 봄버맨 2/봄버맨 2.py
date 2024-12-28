# 폭탄 칸 + 인접한 4칸 파괴
# 연쇄 반응 없음
# 1) 일부 칸에 폭탄 설치 - 폭탄이 설치된 시간 동일
# 2) 다음 1초동안 아무것도 하지 않음
# 3) 다음 1초동안 폭탄이 설치되어 있지 않는 모든 칸에 폭탄 설치 > 모든 칸에 폭탄 존재
# 4) 1초가 지난 후에 3초 전에 설치한 폭탄 모두 폭발
# 3) <-> 4) 반복

# 0초
# ...
# .0.
# ...
# 1초
# ...
# .0.
# ...
# 2초
# 000
# 000
# 000
# 3초 -> 3초 전에 설치된 폭탄 붐! -> 3초 전 = 0초
# 0.0
# ...
# 0.0

n, m, t = map(int, input().split())
board = [list(input()) for _ in range(n)]

def solution(n, m, t, board):
    
    time_board = [[-1 for _ in range(m)] for _ in range(n)]
    
    # 각 폭탄의 시간이 기록 필요
    
    def find_bomb():
        grids = []
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O':
                    grids.append((r, c))
        return grids
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def bomb(r, c):
        dr = [-1, 1, 0, 0, 0]
        dc = [0, 0, -1, 1, 0]
        # print("여기")
        for k in range(5):
            nr = r + dr[k]
            nc = c + dc[k]
            if in_range(nr, nc):
                board[nr][nc] = '.'
                time_board[nr][nc] = -1
                    
    # 빈 칸 제외 폭탄이 설치된 곳의 시간 증가
    def time_up():
        for i in range(n):
            for j in range(m):
                if time_board[i][j] != -1:
                    time_board[i][j] += 1
                    
    # 타임보드에 폭탄의 설치 시간 기록
    def write_bomb_time(bomb_grid, t):
        for grid in bomb_grid:
            i, j = grid
            if time_board[i][j] == -1:
                time_board[i][j] = 0
    # 
    def build_bomb():
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    
    def get_bomb_bomb():
        grids = []
        for i in range(n):
            for j in range(m):
                if time_board[i][j] == 3:
                    grids.append((i, j))
        return grids
                    
    # 3) <-> 4) 과정만 반복하니까 0 1는 기초 상태 기록용
    # 아무것도 하지않는 경우는 처음만 존재
    # 4 이후 주기성!
    if t > 4:
        t = t % 4 + 4
    time = 0
    while True:
        if t == time - 1:
            # print(f"끝: {time}")
            for row in board:
                print(''.join(row))
            # print("-")
            break
        if time == 0:
            grids = find_bomb()
            write_bomb_time(grids, time)
        elif time == 1:
            time_up()
        else:
            time_up()
            if time % 2 == 0:
                build_bomb()
                grids = find_bomb()
                write_bomb_time(grids, time)
            else:
                grids = get_bomb_bomb()
                for grid in grids:
                    i, j = grid
                    bomb(i, j)
        # print(f"time: {time}")
        # print(f"폭탄 좌표 : {grids}" )
        # print("폭탄 보드")
        # for row in board:
        #     print(*row)
        # print("-")
        # print("시간 보드")
        # for row in time_board:
        #     print(*row)
        # print("-")
    
        time += 1
        
solution(n, m, t, board)
