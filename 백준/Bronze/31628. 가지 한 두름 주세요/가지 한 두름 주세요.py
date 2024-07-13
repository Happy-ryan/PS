def solution(board):
    # 열 판단
    for r in range(10):
        start = board[r][0]
        cnt = 1
        for c in range(1, 10):
            if start == board[r][c]:
                cnt += 1
        if cnt == 10:
            return 1
    # 행 판단
    for c in range(10):
        start = board[0][c]
        cnt = 1
        for r in range(1, 10):
            if start == board[r][c]:
                cnt += 1
        if cnt == 10:
            return 1
        
    return 0

board = [list(input().split()) for _ in range(10)]
print(solution(board))