while True:
    try:
        n = int(input())
        dp = [0] * 252
        # dp[i] 2*i 직사각형을 채우는 방법의 수
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3
        for i in range(3,252):
            dp[i] = dp[i-1] + 2*dp[i-2]
        print(dp[n])
    except:
        break