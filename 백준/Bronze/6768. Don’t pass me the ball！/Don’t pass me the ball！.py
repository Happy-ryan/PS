n = int(input())

def solution(n):
    if n < 4:
        return 0

    # (n - 3)C3 <= 조합
    dp = [0] * 101
    dp[0] = 1
    for i in range(1, 101):
        dp[i] = i * dp[i - 1]
        
    return dp[n - 1] // (dp[3] * dp[n - 1 - 3])

print(solution(n))