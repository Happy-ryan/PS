t = int(input())

def solution(N, M, board, qs):
    event = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    
    # 1) 증감 event 기록
    for q in qs:
        r1, c1, r2, c2, v = q # 1base
        event[r1 - 1][c1 - 1] += v # event 발생
        event[r1 - 1][c2] += -v # event 미발생
        event[r2][c1 - 1] += -v # event 미발생
        event[r2][c2] += v # event 미발생 지역이 겹쳐, 2번 중복으로 - 발생해서 +로 보정해야함!!!

    
    # 2) 복구 - 누적합
    psum = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            psum[i + 1][j + 1] = event[i][j] + psum[i + 1][j] + psum[i][j + 1] - psum[i][j]
    
    for i in range(N):
        for j in range(N):
            board[i][j] += psum[i + 1][j + 1]
    
    row, col = [], []
    
    def cal_row():
        for ro in board:
            row.append(sum(ro))
    
    def cal_col():
        for j in range(N):
            val = 0
            for i in range(N):
                val += board[i][j]
            col.append(val)
    
    cal_row()
    cal_col()
    
    print(*row)
    print(*col)


for _ in range(t):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    qs = [list(map(int, input().split())) for _ in range(M)]
    solution(N, M, board, qs)