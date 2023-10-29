# https://www.acmicpc.net/problem/10830

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
mod = 1000

# 행렬의 곱셉 연산
def matix_dot(board1, board2):
    i, k = len(board1), len(board1[0])
    k, j = len(board2), len(board2[0])
    result = [[0 for col in range(j)] for row in range(i)]
    
    for i_ in range(i):
        for j_ in range(j):
            for k_ in range(k):
                result[i_][j_] += (board1[i_][k_] * board2[k_][j_])%mod
            result[i_][j_] %= mod
    return result

# 행렬의 제곱
def matrix_power(board):
    # 행렬은 정사각행렬을 전제함(n by n)
    n = len(board)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                result[i][j] += (board[i][k] * board[k][j])%mod
            result[i][j] %= mod
    return result

# 단위행렬
ret = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            ret[i][j] = 1
            
# 행렬의 거듭제곱 & 비트연산
while m:
    if m & 1 == 1:
        ret = matix_dot(ret, board)
    m >>= 1
    board = matrix_power(board)
    
for row in ret:
    print(*row)