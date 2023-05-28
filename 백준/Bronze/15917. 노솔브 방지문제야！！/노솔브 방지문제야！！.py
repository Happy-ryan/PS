import sys
input = sys.stdin.readline

t = int(input())
def dp(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1]
        
    return dp

dp_list = dp(31)
for _ in range(t):
    a = int(input())
    if a in dp_list: print(1)
    else: print(0)