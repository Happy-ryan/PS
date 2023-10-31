mod =  1000000007

def matrix_plus(mat1, mat2):
    r, c = len(mat1), len(mat1[0])
    for i in range(r):
        for j in range(c):
            mat1[i][j] = mat1[i][j] + mat2[i][j]
            
    return mat1

def matrix_dot(mat1, mat2):
    r, mid = len(mat1), len(mat1[0])
    mid, c = len(mat2), len(mat2[0])
    
    result = [[0 for _ in range(c)] for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            for k in range(mid):
                result[i][j] += (mat1[i][k] * mat2[k][j]) % mod
            result[i][j] %= mod
    
    return result

def matrix_power(matrix, x):
    k = len(matrix)
    ret = [[0 for _ in range(k)] for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if i == j:
                ret[i][j] = 1
    while x:
        if x & 1 == 1:
            ret = matrix_dot(matrix, ret)
        x >>= 1
        matrix = matrix_dot(matrix, matrix)
    
    return ret

n = int(input())
fibo_matrix = [ [1, 1],
                [1, 0]
                ]
fibo_default = [ [1],
                [0]
                ]

res = matrix_dot(matrix_power(fibo_matrix, n), fibo_default)
if n % 2 == 0:
    print(*res[-1])
else:
    print(*res[0])