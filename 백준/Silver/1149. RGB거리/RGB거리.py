n = int(input())
arr = [list(map(int,input().split())) for row in range(n)]
# print(arr)
# 이 문제의 포인트 : 같은 색깔 외의 비용을 더하는 데 경우가 2개가 나온다.
# 따라서 두 경우 중 작은 값을 dp로 넣으면 된다.
# 예를 들어, 1행0열 = arr의 1행0열의 값+min(dp의 0행 1열,dp의 0행 2열)
# 정리 : dp[i][0] = arr[i][0] + min(dp[i-1][1],dp[i-1][2])
# 정리 : dp[i][1] = arr[i][1] + min(dp[i-1][0],dp[i-1][2])
# 정리 : dp[i][2] = arr[i][2] + min(dp[i-1][0],dp[i-1][1])
# 정답 : min(dp[n-1])
dp = [[0 for col in range(3)] for row in range(n)]
# print(dp)
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]
for i in range(1,n):
    dp[i][0] = arr[i][0] + min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = arr[i][1] + min(dp[i-1][0],dp[i-1][2])
    dp[i][2] = arr[i][2] + min(dp[i-1][0],dp[i-1][1])
# print(dp)
print(min(dp[n-1]))