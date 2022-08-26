T = int(input())
# dp 정의
# dp[n][1] dp[n][2] dp[n][3]
# n 을 만들 때 반드시 1로 시작하는 오름차순 배열의 수를 의미
# n 오름차순 정렬을 해야하므로 1로 시작하면 1 2 3 으로 시작하는 오름차순 배열
# n 오름차순 정렬을 해야하므로 2로 시작하면 2 3 으로 시작하는 오름차순 배열
def dp(n):
    dp = [[0 for col in range(4)] for row in range(10004)]
    dp[1][1], dp[1][2], dp[1][3] = 1, 0, 0
    dp[2][1], dp[2][2], dp[2][3] = 1, 1, 0
    dp[3][1], dp[3][2], dp[3][3] = 2, 0, 1
    for i in range(4,n+1):
        dp[i][1] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
        dp[i][2] = dp[i-2][2] + dp[i-2][3]
        dp[i][3] = dp[i-3][3]

    return sum(dp[n])

for test in range(T):
    print(dp(int(input())))