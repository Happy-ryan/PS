from collections import deque
import sys
import math

input = sys.stdin.readline

n, m, R = map(int, input().split())
# min(n, m) % 2 = 0
# 최솟값은 반드시 짝수
board = [list(map(int, input().split())) for _ in range(n)]


# 2차원 회전 - 좌표집합 밀기로 접근
def extract(r1, c1, r2, c2):
    dq = deque([])
    for col in range(c1, c2 + 1):
        dq.append((r1, col))
    for row in range(r1 + 1, r2 + 1):
        dq.append((row, c2))
    for col in range(c2 - 1, c1 - 1, -1):
        dq.append((r2, col))
    for row in range(r2 - 1, r1, -1):
        dq.append((row, c1))
    return dq


def rotate(dq):
    tmps = deque([])
    for r, c in dq:
        tmps.append(board[r][c])
    tmps.rotate(-1)
    for idx, (r, c) in enumerate(dq):
        board[r][c] = tmps[idx]


k = min(n, m) // 2

cr, cc = 0, 0
r1 = cr
c1 = cc
r2 = cr + n - 1
c2 = cc + m - 1


def simulate(r1, c1, r2, c2):
    if r1 == k and c1 == k:
        return

    dq = extract(r1, c1, r2, c2)
    rotate(dq)

    simulate(r1 + 1, c1 + 1, r2 - 1, c2 - 1)


# r에 대한 주기파악 > 최소공배수 > 최소공배수만큼 돌면 맨처음 상태로 돌아옴
mod = 1
for r in range(k):
    num = m * 2 + (n - 2) * 2
    mod = mod * num // math.gcd(mod, num)

    m -= 2
    n -= 2

R %= mod

for _ in range(R):
    simulate(r1, c1, r2, c2)

for row in board:
    print(*row)