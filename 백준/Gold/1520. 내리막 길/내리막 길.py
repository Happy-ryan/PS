# https://www.acmicpc.net/problem/1520

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M
# 항상 높이가 더 낮은 지점으로만 이동하여 목표지점으로 이동!
# dpf(r, c): (0, 0)에서 (r, c)까지의 경우의 수 > DP를 생각할 수 있다!!
# dpf(r, c) = dpf(pre_r, pre_c) + 1 where board[pre_r][pre_c] > board[r][c]
def dpf(r: int, c: int):
    if dp[r][c] != -1:
        return dp[r][c]

    ret = 0
    for k in range(4):
        pre_r, pre_c = r + dr[k], c + dc[k]
        if in_range(pre_r, pre_c) and board[pre_r][pre_c] > board[r][c]:
            ret += dpf(pre_r, pre_c)
            # print(f"pre_r: {pre_r}, pre_c: {pre_c}, board: {board[pre_r][pre_c]}")

    # 시작점은 (0, 0)
    if r == 0 and c == 0:
        return 1

    dp[r][c] = ret

    return ret

print(dpf(N - 1, M - 1)) 