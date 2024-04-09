n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

from itertools import product
from copy import deepcopy


def solution(n, m, board):

    MAX_NUM = max(n, m)

    # cctv의 좌표후보 선정 - 최대 8개
    def get_cctv_grid():
        grids = []
        for r in range(n):
            for c in range(m):
                if board[r][c] != 0 and board[r][c] != 6:
                    grids.append((board[r][c], r, c))
        return grids

    def arrange_dir(grid_cnt):
        # 중복조합이 필요하다!! > 중복조합이 아니라 중복순열이 와야한다.
        # 왜냐하면 각 좌표에 어떤 방향이 제시되는지에 따라 감시당하는 영역이 완전히 달라지기 때문이다.
        total_dir = []
        for row in product([0, 1, 2, 3], repeat = grid_cnt):
            total_dir.append(row)

        return total_dir

    guide_dirs = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}

    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m

    # 한 지점이 선택할 수 있는 방향 4개
    # 4^8 = 6만
    # 2번의 경우 유효 방향은 사실 2개 / 5번의 경우 유효 방향은 사실 1개
    # dir은 ㅁ -> 이 0방향이 기준이다. 반시계방향으로 방향 처리하기
    # 동(0) 북(1) 서(2) 남(3)
    # type 2의 경우 dir % 4, (dir + 2) % 4
    # type 3의 경우 dir % 4, (dir + 1) % 4
    # type 4의 경우 dir % 4, (dir + 1) % 4, (dir + 2) % 4
    # type 5의 경우 dir % 4, (dir + 1) % 4, (dir + 2) % 4,  (dir + 3) % 4

    def being_watched(r, c, dirs, board):
        for dir in dirs:
            for k in range(1, MAX_NUM):
                nr = r + guide_dirs[dir][0] * k
                nc = c + guide_dirs[dir][1] * k
                if in_range(nr, nc) and board[nr][nc] == 6:
                    break
                # print(
                #     f"r: {r}, c: {c}, || dir: {dir}, guide_dirs[dir]: {guide_dirs[dir]}  ||  nr: {nr}, nc: {nc}"
                # )
                if in_range(nr, nc) and (board[nr][nc] == 0 or board[nr][nc] == '#'):
                    board[nr][nc] = "#"

    def view(type, r, c, cur_dir, board):
        if type == 1:
            dirs = [cur_dir % 4]
            being_watched(r, c, dirs, board)
        elif type == 2:
            dirs = [cur_dir % 4, (cur_dir + 2) % 4]
            being_watched(r, c, dirs, board)
        elif type == 3:
            dirs = [cur_dir % 4, (cur_dir + 1) % 4]
            being_watched(r, c, dirs, board)
        elif type == 4:
            dirs = [cur_dir % 4, (cur_dir + 1) % 4, (cur_dir + 2) % 4]
            being_watched(r, c, dirs, board)
        elif type == 5:
            dirs = [
                cur_dir % 4,
                (cur_dir + 1) % 4,
                (cur_dir + 2) % 4,
                (cur_dir + 3) % 4,
            ]
            being_watched(r, c, dirs, board)

    def cal_zero(board):
        cnt = 0
        for r in range(n):
            for c in range(m):
                if board[r][c] == 0:
                    cnt += 1
        return cnt

    cctv_grid = get_cctv_grid()
    combination_dirs = arrange_dir(len(cctv_grid))

    # print(cctv_grid)
    # print(combination_dirs)

    answer = n * m + 1
    for cur_dirs in combination_dirs:
        # print(f"방향 조합: {cur_dirs}")
        new_board = deepcopy(board)
        for idx, cur_dir in enumerate(cur_dirs):
            type, r, c = cctv_grid[idx]
            view(type, r, c, cur_dir, new_board)
        # for row in new_board:
        #     print(*row)
        answer = min(answer, cal_zero(new_board))
        # print(f"------{cal_zero(new_board)}----")

    return answer


print(solution(n, m, board))