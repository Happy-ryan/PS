# https://www.acmicpc.net/problem/12849
D = int(input())
matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]
l = len(matrix)
# 행렬의 곱셉
mod = 1000000007
def matrix_dot(mat1, mat2):
    row, k = len(mat1), len(mat1[0])
    k, col = len(mat2), len(mat2[0])
    result = [[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            for k_ in range(k):
                result[i][j] += (mat1[i][k_] * mat2[k_][j])%mod
            result[i][j] %= mod
    return result

# 단위행렬
ret = [[0 for _ in range(l)] for _ in range(l)]
for i in range(l):
    for j in range(l):
        if i == j:
            ret[i][j] = 1
            
# 행렬의 거듭제곱 & 분할정복(비트연산)
while D:
    if D & 1 == 1:
        ret = matrix_dot(ret, matrix)
    D >>= 1
    matrix = matrix_dot(matrix, matrix)
    
print(ret[0][0])