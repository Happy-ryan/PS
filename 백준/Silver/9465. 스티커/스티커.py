T = int(input())
# dp[n][0](0 based) n번째 줄에서 아무것도 선택하지 않을 때의 점수
# dp[n][1](0 based) n번째 줄에서 위쪽 스티커를 선택했을 때의 점수
# dp[n][2](0 based) n번째 줄에서 아래쪽 스티커를 선택했을 때의 점수
for _ in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for  row in range(2)]
    dp = [[0 for col in range(3)] for row in range(n)]
    dp[0][0],dp[0][1],dp[0][2] = 0, arr[0][0], arr[1][0]
    for i in range(1,n):
        dp[i][0] += max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
        dp[i][1] += (arr[0][i]+max(dp[i-1][0],dp[i-1][2])) # 스티커 위쪽(0행) 선택 후 i-1까지의 최대 합을 더하기 
        # 위쪽 스티커 선택했으므로 i-1번째 줄에서 선택할 수 있는 점수는 선택하지 않은 dp[i-1][0] 과
        # dp[i-1][2] 밑에서 선택한 점수, 2개가 있고 거기서 최대값을 가져온다.
        dp[i][2] += (arr[1][i]+max(dp[i-1][0],dp[i-1][1]))
    print(max(dp[n-1]))