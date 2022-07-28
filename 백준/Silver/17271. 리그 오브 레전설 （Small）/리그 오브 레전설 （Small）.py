N,M = map(int,input().split())
dp = [0]*(10004)
mod = 1000000007
# dp[i] i초 일 때 쓸 수 있는 스킬이 조합
dp[1] = 1
dp[M] = 2 # 스킬B를 나타낼 수 있는 경우의 수는 : A로만 나타내거나 B 1번을 쓰는 경우만 존재
for i in range(2,10004):
    if i != M:
        dp[i] = (dp[i-1] + dp[i-M])%mod
print(dp[N])