n = int(input())
arr = [ input() for col in range(n)]
arr = [float(a) for a in arr]
# print(arr)
# dp[i] 인덱스i를 반드시 선택했을 때 연속된 곱의 최댓값
dp = [0]*10004
dp[0] = arr[0]
for i in range(1,n):
    dp[i] = max(arr[i],arr[i]*dp[i-1])
print('{0:0.3f}'.format(max(dp)))