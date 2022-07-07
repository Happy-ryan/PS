n = int(input())
arr = list(map(int,input().split()))
dp = [0] * 100006
#dp[i] 인덱스(0~n-1) i을 반드시 선택했을 때의 연속합의 최대값 
dp[0] = arr[0]
# dp[1] 인덱스 1반드시 선택했을 때 arr[1] 단독이 더 크냐 연속합이 더 크냐 판단해서 갱신해주는 것.
for i in range(1,n):
    dp[i] = max(arr[i],dp[i-1]+arr[i])

print(max(dp[:n]))