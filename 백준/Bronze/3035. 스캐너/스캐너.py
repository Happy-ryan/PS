R, C, ZR, ZC = map(int, input().split())
mat = [list(input()) for row in range(R)]
new_mat = [[0 for col in range(C * ZC)] for row in range(R * ZR)]

for i in range(R*ZR):
  for j in range(C*ZC):
       new_mat[i][j] = mat[i//ZR][j//ZC]

for row in new_mat:
    print(''.join(row))