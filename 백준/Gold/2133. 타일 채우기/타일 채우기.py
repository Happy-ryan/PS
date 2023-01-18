import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 0
# n이 홀수일 때는 타일을 채울 수 없다.
# n이 홀수면 면적 3 * n > 홀수
# 나무도착 하나의 넓이 2이므로 짝수 + 짝수 +... + 짝수 = (무조건) 짝수
for k in range(2, n + 1, 2):
    for x in range(2, k + 1, 2):
        if x == 2:
            dp[k] += dp[k - x] * 3
        else:
            dp[k] += dp[k - x] * 2

print(dp[n])