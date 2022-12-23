def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    if n == 1:
        return 0
    dp[0] = 1
    dp[2] = 3
    # n이 홀수인 경우 직사각형의 면적 3*n으로 홀수가 나온다.
    # 각 나무토막의 넓이는 2이므로 절대로 가로가 홀수인 경우에는 전체를 채울 수 없다.
    for k in range(4, n+1, 2):
        for x in range(2, k+1, 2):
            if x == 2:
                dp[k] += 3 * dp[k - x]
            else:
                dp[k] += 2 * dp[k - x]
    
    answer = dp[n]
    return answer

N = int(input())
print(solution(N))