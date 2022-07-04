dp = [0]*10004
# dp[i] i번째 피보나치수ㅇ
dp[1] = 1
dp[2] = 1
for i in range(3,10001):
    dp[i] = dp[i-1] + dp[i-2]

T = int(input())
for i in range(1,T+1):
    P,Q = map(int,input().split())
    print('Case #%s:' %i ,dp[P]%Q )