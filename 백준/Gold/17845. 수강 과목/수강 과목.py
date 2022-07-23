N,K = map(int,input().split())
arr = [ list(map(int,input().split())) for row in range(K)]
dp = [[-1 for col in range(N+1)] for row in range(K+1)]
dp[0][0] = 0
for i in range(1,K+1):
    dp[i] = dp[i-1].copy()
    for j in range(N+1):
        if dp[i-1][j] >= 0 and j + arr[i-1][1] <= N:
            dp[i][j+arr[i-1][1]] = max(dp[i][j+arr[i-1][1]], dp[i-1][j]+arr[i-1][0])
            # dp[i][j+arr[i-1][0] : 딥카피로 i-1행에 있던 j+arr[i-1][0] 열의 가치를 가져온 것
            # dp[i-1][j] + arr[i-1][0] : dp[i-1][j] + arr[i-1][1] : i-1행j열 >= 0 and j+arr[i-1][1]<=N 넣을 수 있는데 
                                    #   우연히 j + arr[i-1][1] 열에 위치해 딥카피한 값과 동일한 위치에 존재하게된 경우
            # i 행의 j+arr[i-1][0] 열에 2가지 값이 온다.

print(max(dp[K]))