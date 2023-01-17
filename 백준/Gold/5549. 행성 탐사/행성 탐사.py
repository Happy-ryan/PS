import sys
input = sys.stdin.readline

r, c = map(int, input().split())
t = int(input())
A = [list(input()) for row in range(r)]

A_J = [[0 for col in range(c)] for row in range(r)]
A_O = [[0 for col in range(c)] for row in range(r)]
A_I = [[0 for col in range(c)] for row in range(r)]

for i in range(r):
    for j in range(c):
        if A[i][j] == 'J':
            A_J[i][j] = 1
        elif A[i][j] == 'O':
            A_O[i][j] = 1
        if A[i][j] == 'I':
            A_I[i][j] = 1

def prefixSum(r, c, A):
    psum = [[0 for col in range(c + 1)] for row in range(r + 1)]
    for i in range(r):
        for j in range(c):
            psum[i + 1][j + 1] = psum[i][j + 1] + psum[i + 1][j] - psum[i][j] + A[i][j]
    
    return psum

def RangeSum(r0, c0, r1, c1, psum):
    # r0 < r1, c0 < c1
    cnt = psum[r1][c1] - psum[r1][c0 - 1] - psum[r0 - 1][c1] + psum[r0 - 1][c0 - 1]
    return cnt

psum_J = prefixSum(r, c, A_J)
psum_O = prefixSum(r, c, A_O)
psum_I = prefixSum(r, c, A_I)

for _ in range(t):
    r0, c0, r1, c1 = map(int, input().split())
    print(RangeSum(r0, c0, r1, c1, psum_J), RangeSum(r0, c0, r1, c1, psum_O), RangeSum(r0, c0, r1, c1, psum_I))