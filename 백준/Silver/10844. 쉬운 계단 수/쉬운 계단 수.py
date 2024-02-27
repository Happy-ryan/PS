n = int(input())

def solution(n):
    # dp[i][j] i번자리수일 때 마지막 수가 j일 때 만들어지는 계단수의 개수
    inf = int(1e9)
    dp = [[-inf for _ in range(10)] for _ in range(n + 1)]
    mod = 1000000000
    dp[0][0] = 0
    for i in range(1, n + 1):
        if i == 1:
            for j in range(10):
                if j == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
        else:
            for j in range(10):
                if j == 0:
                    dp[i][j] = (dp[i - 1][j + 1]) % mod
                elif j == 9:
                    dp[i][j] = (dp[i - 1][j - 1]) % mod
                else:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod
                    
    return (sum(dp[n])) % mod
        
print(solution(n))