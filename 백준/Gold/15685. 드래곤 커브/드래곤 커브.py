M = 101
N = int(input())

# 모든 드래곤커브 기록 board
result_board = [[False for _ in range(M)] for _ in range(M)]

# 만든 보드 기록
def apply_board(target_board, source_board):
    for r in range(M):
        for c in range(M):
            if source_board[r][c]:
                target_board[r][c] = True
# 격자 내 범위 체크
def in_range(r, c, M):
    return 0 <= r < M and 0 <= c < M
# 시계방향 회전
# 좌표 : (1, 0) c = c*, r = r*  // (0, -1) c = r*, r = -c*
# r0 c0 : 회전의 중심 축
def rotate(r, c, r0, c0):
    r -= r0
    c -= c0 # 회전축을 원점으로 재조정
    nr = -c # 시계방향 회전
    nc = r
    nr += r0
    nc += c0 # (r0, c0)를 회전축으로 재조정
    return nr, nc
# 51번 - 만들었던 보드에 회전 적용하기
def generate(y, x, ey, ex, board):
    rotated_board = [[False for _ in range(M)] for _ in range(M)]
    for r in range(M):
        for c in range(M):
            if board[r][c]:
                nr, nc = rotate(r, c, ey, ex)
                if in_range(nr, nc, M):
                    rotated_board[nr][nc] = True
    apply_board(board, rotated_board)

    return rotate(y, x, ey, ex)


dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

for _ in range(N):
    y, x, d, g = map(int, input().split())
    # 드래곤마다 새로운 board 생성
    board = [[False for _ in range(M)] for _ in range(M)]
    # 방향성에 따른 다음 좌표
    # 드래곤 시작점 - y x
    # 다음 좌표가 필요한 이유 ny nx - 회전축이 된다.
    ny, nx = y + dy[d], x + dx[d]
    board[y][x] = True
    board[ny][nx] = True

    # 드래곤 키우기
    for _ in range(g):
        ny, nx = generate(y, x, ny, nx, board)
    
    apply_board(result_board, board)

cnt = 0
for r in range(1, M):
    for c in range(1, M):
        if result_board[r-1][c-1] and result_board[r-1][c] and result_board[r][c-1] and result_board[r][c]:
            cnt += 1
print(cnt)