R, C, ZR, ZC = map(int, input().split())
mat = [list(input()) for row in range(R)]
new_mat = [[0 for col in range(C * ZC)] for row in range(R * ZR)]

for r0 in range(R):
    for c0 in range(C):
        x = mat[r0][c0]
        for r1 in range(r0 * ZR, r0 * ZR + ZR):
            for c1 in range(c0 * ZC, c0 * ZC + ZC):
                new_mat[r1][c1] = x

for row in new_mat:
    print(''.join(row))