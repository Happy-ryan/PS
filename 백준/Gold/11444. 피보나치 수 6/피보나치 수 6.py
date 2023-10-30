# https://www.acmicpc.net/problem/11444
# 피보나치와 행렬
# ([1, 1],  ([[fn+1],  ([[fn+2], 
#  [1, 0])   [fn]])     [fn+1]]) 

n = int(input())
mod = 1000000007
default = [ [1],
            [0]]
matrix = [  [1, 1],
            [1, 0]]


def matrix_dot(mat1, mat2):
    r, k = len(mat1), len(mat1[0])
    k, c = len(mat2), len(mat2[0])
    res = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for k_ in range(k): 
                res[i][j] += (mat1[i][k_] * mat2[k_][j]) % mod
            res[i][j] %= mod
    return res

def matrix_power(matrix, x:int):
    # 정사각행렬을 전제함.
    l = len(matrix)
    # 단위행렬
    ret = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            if i == j:
                ret[i][j] = 1
    # 거듭제곱 by 비트연산
    while x:
        if x & 1 == 1:
            ret = matrix_dot(matrix, ret)
        x >>= 1
        matrix = matrix_dot(matrix, matrix)
        
    return ret

matrix_ = matrix_power(matrix, n)
print(*matrix_dot(matrix_, default)[-1])