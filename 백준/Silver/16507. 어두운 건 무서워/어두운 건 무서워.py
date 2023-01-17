
import pprint
r, c, t = map(int, input().split())
A = [list(map(int, input().split())) for row in range(r)]

psum = [[0 for col in range(c + 1)] for row in range(r + 1)]
for i in range(r):
    for j in range(c):
        psum[i + 1][j + 1] = psum[i + 1][j] + psum[i][j + 1] - psum[i][j] + A[i][j] #psum 0을 채웠으므로.

# pprint.pprint(psum)

for _ in range(t):
    r0, c0, r1, c1 = map(int, input().split())
    cnt = (r1 - r0 + 1) * (c1 - c0 + 1) # 정사각형의 수
    RangeSum = psum[r1][c1] + psum[r0 - 1][c0 - 1] - psum[r1][c0 - 1] - psum[r0 - 1][c1]
    print(RangeSum//cnt)