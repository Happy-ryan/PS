N,M,K = map(int,input().split())
# 팩토리얼 - dp
dp = [0] * (N+M+1)
dp[0] = 1
dp[1] = 1
for i in range(2,N+M+1):
    dp[i] = i*dp[i-1]

if K == 0:
    print(dp[N+M-2]//(dp[N-1]*dp[M-1]))
else:
    # K의 인덱스 파악
    j = (K-1)%M
    i = (K-1)//M
    case1 = dp[i+j]//(dp[i]*dp[j])
    case2 = dp[N-1+M-1-i-j]//(dp[N-1-i]*dp[M-1-j])
    print(case1*case2)