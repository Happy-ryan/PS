# https://www.acmicpc.net/problem/14503

n, m = map(int, input().split())
r, c, dir = map(int, input().split())
board = [list(map(int, input().split())) for row in range(n)]

dirs = [(-1, 0), # 북
        (0, 1), # 동
        (1, 0), # 남
        (0, -1)] # 서

def clean_check(r, c, board):
    flag = True
    if board[r][c+1] == 0 or board[r][c-1] == 0 or board[r + 1][c] == 0 or board[r-1][c] == 0:
        flag = False
    return flag
    
def change_dir(r, c, dir, board):
    # 내 방향 먼저 쭈욱 가는게 아니라 "반시계 방향으로 먼저" 돌아야한다.(주의!)
    # 문제가 정의한 방향 : 북 -> 동 -> 남 -> 서 : 시계방향
    # 따라서 현재 dir 에  반시계 회전을 위해서 +3 을 더해야한다.
    dir += 3
    while True:
        dir = dir % 4
        nr, nc = r + dirs[dir][0], c + dirs[dir][1]
        # 벽이거나 청소했으면...반시계방향 체인지
        if board[nr][nc] != 0:
            dir += 3
        else:
            break
    return dir
    
cnt = 0
def solution(cr, cc, dir, dirs, board):
    global cnt
        
    if board[cr][cc] == 0:
        board[cr][cc] = 2
        cnt += 1
        
    # 청소 안 한 칸이 존재하지 않음
    if clean_check(cr, cc, board):
        nr, nc = cr - dirs[dir][0], cc - dirs[dir][1]
        if board[nr][nc] == 1:
            # print("벽 만나서 종료!")
            return cnt
        else:
            return solution(nr, nc, dir, dirs, board)
    else:
        dir = change_dir(cr, cc, dir, board)
        nr, nc = cr + dirs[dir][0], cc + dirs[dir][1]
        return solution(nr, nc, dir, dirs, board)

print(solution(r, c, dir, dirs, board))