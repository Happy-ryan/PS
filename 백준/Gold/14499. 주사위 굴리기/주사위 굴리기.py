# https://www.acmicpc.net/problem/14499
n, m, cr, cc, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(int, input().split()))

# 동(0)남(1)서(2)북(3)
def chang_direction(cur_dir):
    if cur_dir == 4:
        cur_dir = 1
    elif cur_dir == 1:
        cur_dir = 0
    return cur_dir
# 격자 내 이동
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 초기 주사위 상태(바닥, 윗면, 서쪽, 동쪽, 북쪽, 남쪽)
# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다. 
dices = [0, 0, 0, 0, 0, 0]
# 현재 바닥(1 - 0), 윗면(6 - 1) / 서쪽면(4 - 2), 동쪽면(3 - 3) / 북쪽면(2 - 4), 남쪽면(5 - 5)
# 남쪽(4 - 100 -> 001)으로 굴림 : 바닥(5), 윗면(2) / 서쪽(4), 동쪽(3) / 북쪽(1), 남쪽(6)
# 북쪽(3 - 11)으로 굴림 : 바닥(2), 윗면(5) / 서쪽(4), 동쪽(3) / 북쪽(6), 남쪽(1)
# 서쪽(2 - 10)으로 굴림 : 바닥(4), 윗면(3) / 서쪽(6), 동쪽(1) / 북쪽(2), 남쪽(5)
# 동쪽(1 - 01 -> 00)으로 굴림 : 바닥(3), 윗면(4) / 서쪽(1), 동쪽(6) / 북쪽(2), 남쪽(5)
def simulate_S(dices):
    dices = [dices[5], dices[4], dices[2], dices[3], dices[0], dices[1]]
    return dices

def simulate_N(dices):
    dices = [dices[4], dices[5], dices[2], dices[3], dices[1], dices[0]]
    return dices

def simulate_W(dices):
    dices = [dices[2], dices[3], dices[1], dices[0], dices[4], dices[5]]
    return dices

def simulate_E(dices):
    dices = [dices[3], dices[2], dices[0], dices[1], dices[4], dices[5]]
    return dices
# 주사위 방향에 따른 회전시키기
def rotate(cur_dir):
    global dices
    if cur_dir == 0:
        return simulate_E(dices)
    elif cur_dir == 1:
        return simulate_S(dices)
    elif cur_dir == 2:
        return simulate_W(dices)
    else:
        return simulate_N(dices)
# 격자 내 이동 판단
def in_range(r, c):
    return 0 <= r < n and 0 <= c < m
# 시뮬레이션
def simulate(cr, cc, cmds):
    global nr, nc, dices
    for cmd in cmds:
        cur_dir = chang_direction(cmd)
        nr = cr + dr[cur_dir]
        nc = cc + dc[cur_dir]
        if not in_range(nr, nc):
            continue
        else:
            dices = rotate(cur_dir)
            if board[nr][nc] == 0:
                board[nr][nc] = dices[0]
            else:
                dices[0] = board[nr][nc]
                board[nr][nc] = 0
            print(dices[1])
            cr, cc = nr, nc

simulate(cr, cc, cmds)
