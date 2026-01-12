N, M = map(int, input().split())
left_side = list(map(int, input().split()))
up_side = list(map(int, input().split()))

def solution(N, M, left_side, up_side):
    
    board = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]
    
    for ridx in range(N):
        board[ridx + 1][0] = left_side[ridx]
    for cidx in range(M):
        board[0][cidx + 1] = up_side[cidx]
        
    # for row in board:
    #     print(row)
    
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            board[r][c] = 0 if board[r - 1][c] == board[r][c - 1] else 1

    # for row in board:
    #     print(row)
        
    return board[N][M]

print(solution(N, M, left_side, up_side))