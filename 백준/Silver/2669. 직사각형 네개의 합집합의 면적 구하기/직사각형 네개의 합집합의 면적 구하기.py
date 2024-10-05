sqs = [list(map(int, input().split())) for _ in range(4)]

def solution(sqs):
    board = [[0 for _ in range(200)] for _ in range(200)]
    
    # 칸을 색칠함
    cnt = 0
    for sq in sqs:
        r1, c1, r2, c2 = sq
        for i in range(r1, r2):
            for j in range(c1, c2):
                if board[i][j] == 0:
                    board[i][j] = 1
                    cnt += 1
    return cnt

print(solution(sqs))