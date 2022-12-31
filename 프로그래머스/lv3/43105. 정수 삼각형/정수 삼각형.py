# 2차원 dp
def solution(triangle):
    R, C = len(triangle), len(triangle[-1])
    dp = [[0 for col in range(C)] for row in range(R)]
    dp[0][0] = triangle[0][0]
    for r in range(1, R):
        # c의 범위를 C라고 쓰면 1행 2열도 구하게 되버린다. out of range
        # 따라서 길이만큼만 dp를 구해야한다.
        for c in range(0, len(triangle[r])):
            if c == 0:
                dp[r][c] = dp[r - 1][c] + triangle[r][c]
            elif c == r:
                dp[r][c] = dp[r - 1][c - 1] + triangle[r][c]
            else:
                dp[r][c] = max(dp[r-1][c-1], dp[r-1][c]) + triangle[r][c]
    return max(dp[R-1])