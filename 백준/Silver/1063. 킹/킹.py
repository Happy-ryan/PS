king, stone, n = input().split()
cmds = [input() for _ in range(int(n))]

# 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.
def solution(king, stone, cmds):
    SIZE = 8
    k_board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    s_board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    
    dic = {
        'R': (0, 1),
        'L': (0, -1),
        'B': (1, 0),
        'T': (-1, 0),
        'RT': (-1, 1),
        'LT': (-1, -1),
        'RB': (1, 1),
        'LB': (1, -1)
    }

    # A1 -> 좌표로 변환
    def change_position(target):
        r = SIZE - int(target[1])
        c = ord(target[0]) - 65

        return (r, c)

    # 좌표 -> A1으로 변환
    def recover_position(cr, cc):
        r = SIZE - cr
        c = chr(cc + 65) 

        return c + str(r)

    # 가장 마지막 위치 파악
    def find_final_position(board):
        max_gird = []
        for r in range(8):
            for c in range(8):
                if board[r][c] != 0:
                    max_gird.append((board[r][c], r, c))
        
        max_gird.sort(key=lambda x : x[0])

        return max_gird[-1]
                

    # 나가리 판단
    def in_range(r, c):
        return 0 <= r < SIZE and 0 <= c < SIZE


    k_r, k_c = change_position(king)
    k_board[k_r][k_c] = 1
    s_r, s_c = change_position(stone)
    s_board[s_r][s_c] = 1

    for idx, cmd in enumerate(cmds):
        dr, dc = dic[cmd]
        k_nr = k_r + dr
        k_nc = k_c + dc
        # 킹 나가리
        if not in_range(k_nr, k_nc):
            continue
        if k_nr == s_r and k_nc == s_c:
            s_nr = s_r + dr
            s_nc = s_c + dc

            # 돌 나가리
            if not in_range(s_nr, s_nc):
                continue

            s_r, s_c = s_nr, s_nc

        k_r, k_c = k_nr, k_nc
        # print(f"k_r: {k_r}, k_c: {k_c} | s_r: {s_r}, s_c: {s_c}")

        k_board[k_r][k_c] = idx + 2
        s_board[s_r][s_c] = idx + 2


    # for row in k_board:
    #     print(*row)
    
    _, r, c = find_final_position(k_board)
    # print(r, c)
    print(recover_position(r, c))
    # print("-")
    
    # for row in s_board:
        # print(*row)
    _, r, c = find_final_position(s_board)
    # print(r, c)
    print(recover_position(r, c))

solution(king, stone, cmds)