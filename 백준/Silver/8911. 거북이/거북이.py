def solution(cmds):
    grids = [(0, 0)]
    start = (0, 0)
    # 동(0) 남(1) 서(2) 북(3)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # L : 반시계 회전 / R : 시계 회전
    # 반시계: 북(3) -> 서(2) -> 남(1) -> 동(0)
    dir = 3
    for cmd in cmds:
        cr = grids[-1][0]
        cc = grids[-1][1]
        if cmd == 'F':
            dir = dir 
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            grids.append((nr, nc))
        elif cmd == 'B':
            dir = (dir + 2) % 4
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            grids.append((nr, nc))
            dir = (dir + 2) % 4
        elif cmd == 'L':
            dir = (dir - 1 + 4) % 4
        elif cmd == 'R':
            dir = (dir + 1) % 4

    # print(grids)
    r_grids = set()
    c_grids = set()

    for grid in grids:
        x, y = grid
        r_grids.add(x)
        c_grids.add(y)

    # print(r_grids)
    # print(c_grids)

    return (max(r_grids) - min(r_grids)) * (max(c_grids) - min(c_grids))


t = int(input())
for _ in range(t):
    cmds = list(input())
    print(solution(cmds))