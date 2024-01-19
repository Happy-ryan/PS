# https://www.acmicpc.net/problem/1730

n = int(input())
cmds = input()
# 이동방향을 기록함
move_dir_board = [[[] for _ in range(n)] for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


dir = {'D': (1, 0,),
    'U' : (-1, 0),
    'R' : (0, 1),
    'L' : (0, -1)}


r1, c1 = 0, 0
for cmd in cmds:
    r2, c2 = r1 + dir[cmd][0], c1 + dir[cmd][1]
    # in_range하지 못한 좌표는 명령 무시해야함.
    if in_range(r2, c2):
        # 왜 r1, c1도 방향을 기록해?
        # (0,0)에서 D면 (1,0)이 D방향을 보고 있는 상태임.
        # 즉, 움직임이라는 것은 2칸씩을 쓴다고 볼 수 있음.
        # 그래서 한 움직임 당 2칸씩 move_dir에 기록하고 왼오/상하 서로 다른 소속이면 + 처리
        move_dir_board[r1][c1].append(cmd)
        move_dir_board[r2][c2].append(cmd)
        r1, c1 = r2, c2
        
for r in range(n):
    for c in range(n):
        row = move_dir_board[r][c]
        if ('R' in row or 'L' in row) and ('U' in row or 'D' in row):
            print('+', end='')
        elif ('R' in row or 'L' in row) and not ('U' in row or 'D' in row):
            print('-',end='')
        elif not ('R' in row or 'L' in row) and ('U' in row or 'D' in row):
            print('|',end='')
        else:
            print('.', end='')
    print()