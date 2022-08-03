n = int(input())
arr = [ int(input()) for _ in range(n)]
# print(arr)
# dp[i] i번째 와인을 반드시 먹을 때 3연속 되지 않는 최대 와인의 양
# i번째 와인arr[i]을 선택하고 바로 옆 i-1번째를 선택하는지 안한는지로 구분
dp =[0]*(n+1)
if n==1:
    print(arr[0])
elif n==2:
    print(arr[0]+arr[1])
else:
    dp[1] = arr[0]
    dp[2] = arr[0]+arr[1]
    dp[3] = max(dp[2],arr[2]+arr[1],arr[2]+arr[0])
    for i in range(4,n+1):
        dp[i] = max(dp[i-1],arr[i-1]+arr[i-2]+dp[i-3],arr[i-1]+dp[i-2])

    print(max(dp))