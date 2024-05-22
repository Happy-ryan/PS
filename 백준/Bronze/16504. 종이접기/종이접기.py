n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def solution(n, board):
    sum_val = 0
    for row in board:
        sum_val += sum(row)
    return sum_val

print(solution(n, board))