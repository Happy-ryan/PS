def solution(n):
    answer = 0
    mod = 100000007
    dp = [0] * (n + 1)
    dp[2] = 3
    dp[4] = 11
    # n이 홀수인 경우 직사각형의 면적 3*n으로 홀수가 나온다.
    # 각 나무토막의 넓이는 2이므로 절대로 가로가 홀수인 경우에는 전체를 채울         수 없다.
    for k in range(6, n+1, 2):
        dp[k] = (3 * dp[k - 2] + 2 * dp[k - 4])%mod 
    
    answer = dp[n]
    
    return answer