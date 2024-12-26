n, m, r = map(int, input().split())  # n, m은 짝수
board = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(int, input().split()))


def solution(n, m, r, board, cmds):

    def one(): # 상하반전
        n, m = len(board), len(board[0])
        for r_idx in range(0, n // 2):
            board[r_idx], board[n - r_idx - 1] = board[n - r_idx - 1], board[r_idx]
        return board
        
    def two(): # 좌우반전
        n, m = len(board), len(board[0])
        for r in range(n):
            for c_idx in range(0, m // 2):
                board[r][c_idx], board[r][m - c_idx - 1] = board[r][m - c_idx - 1], board[r][c_idx]
        return board
        
    def three(): # 오른쪽으로 90도 회전
        N, M = len(board), len(board[0])
        new_board = [[0 for _ in range(N)] for _ in range(M)]
        # (5, 0) -> (0, 0)
        # (5, 1) -> (1, 0)
        # (5, 2) -> (2, 0)
        for c in range(M):
            for r in range(N - 1, -1, -1):
                new_board[c][N - r - 1] = board[r][c]
                
        return new_board

    def four(): # 왼쪽으로 90도 회전
        N, M = len(board), len(board[0])
        new_board = [[0 for _ in range(N)] for _ in range(M)]
        # (0, 7) -> (0, 0)
        # (1, 7) -> (0, 1)
        # (2, 7) -> (0, 2)
        for c in range(M - 1, -1, -1):
            for r in range(N):
                new_board[M - c - 1][r] = board[r][c]
        
        return new_board

            
    def five():
        n, m = len(board), len(board[0])
        # 1 -> 2 / 2 -> 3 / 3 -> 4 / 4 -> 1
        points = [(0, 0), (0, m // 2), (n // 2, m // 2), (n // 2, 0)] # 1, 2, 3, 4 그룹의 시작점
        new_board = [[0 for _ in range(m)] for _ in range(n)]
        group1 = [[0 for _ in range(m // 2)] for _ in range(n // 2)]
        group2 = [[0 for _ in range(m // 2)] for _ in range(n // 2)]
        group3 = [[0 for _ in range(m // 2)] for _ in range(n // 2)]
        group4 = [[0 for _ in range(m // 2)] for _ in range(n // 2)]
        
        for idx, point in enumerate(points):
            r, c = point
            if idx == 0:
                for i in range(n // 2):
                    for j in range(m // 2):
                        group1[i][j] = board[i + r][j + c]
            elif idx == 1:
                for i in range(n // 2):
                    for j in range(m // 2):
                        group2[i][j] = board[i + r][j + c]
            elif idx == 2:
                for i in range(n // 2):
                    for j in range(m // 2):
                        group3[i][j] = board[i + r][j + c]
            elif idx == 3:
                for i in range(n // 2):
                    for j in range(m // 2):
                        group4[i][j] = board[i + r][j + c]
        
        for idx, point in enumerate(points):
            r, c = point
            if idx == 0:
                for i in range(n // 2):
                    for j in range(m // 2):
                        new_board[i + r][j + c] = group4[i][j]
            if idx == 1:
                for i in range(n // 2):
                    for j in range(m // 2):
                        new_board[i + r][j + c] = group1[i][j]

            if idx == 2:
                for i in range(n // 2):
                    for j in range(m // 2):
                        new_board[i + r][j + c] = group2[i][j]

            if idx == 3:
                for i in range(n // 2):
                    for j in range(m // 2):
                        new_board[i + r][j + c] = group3[i][j]
                        
        return new_board

    def six():
        n, m = len(board), len(board[0])
        # 1 -> 2 / 2 -> 3 / 3 -> 4 / 4 -> 1
        points = [(0, 0), (0, m // 2), (n // 2, m // 2), (n // 2, 0)] # 1, 2, 3, 4 그룹의 시작점
        new_board = [[0 for _ in range(m)] for _ in range(n)]
        group1 = [[0 for _ in range(m // 2)] for _ in range(n // 2)]
        group2 = [[0 for _ in range(m // 2)] for _ in range(n // 2)]
        group3 = [[0 for _ in range(m // 2)] for _ in range(n // 2)]
        group4 = [[0 for _ in range(m // 2)] for _ in range(n // 2)]
        
        for idx, point in enumerate(points):
            r, c = point
            if idx == 0:
                for i in range(n // 2):
                    for j in range(m // 2):
                        group1[i][j] = board[i + r][j + c]
            elif idx == 1:
                for i in range(n // 2):
                    for j in range(m // 2):
                        group2[i][j] = board[i + r][j + c]
            elif idx == 2:
                for i in range(n // 2):
                    for j in range(m // 2):
                        group3[i][j] = board[i + r][j + c]
            elif idx == 3:
                for i in range(n // 2):
                    for j in range(m // 2):
                        group4[i][j] = board[i + r][j + c]
        
        for idx, point in enumerate(points):
            r, c = point
            if idx == 0:
                for i in range(n // 2):
                    for j in range(m // 2):
                        new_board[i + r][j + c] = group2[i][j]
            if idx == 1:
                for i in range(n // 2):
                    for j in range(m // 2):
                        new_board[i + r][j + c] = group3[i][j]

            if idx == 2:
                for i in range(n // 2):
                    for j in range(m // 2):
                        new_board[i + r][j + c] = group4[i][j]

            if idx == 3:
                for i in range(n // 2):
                    for j in range(m // 2):
                        new_board[i + r][j + c] = group1[i][j]
                        
        return new_board
    
    for k in cmds:
        if k == 1:
            board = one()
        elif k == 2:
            board = two()
        elif k == 3:
            board = three()
        elif k == 4:
            board = four()
        elif k == 5:
            board = five()
        elif k == 6:
            board = six()
        # print("k :", k)
        # for row in board:
        #     print(*row)
        # print("-" * 10)
            
    return board

board = solution(n, m, r, board, cmds)
for row in board:
    print(*row)