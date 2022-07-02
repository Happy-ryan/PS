T = int(input())
arr = [int(input()) for row in range(T)]
dp = [0] * 303
dp[0] = arr[0] # 첫 번째 계단의 인덱스 = 0

if T == 1:
    print(arr[0])
elif T ==2:
    print(arr[0]+arr[1]) 
else:
    dp[1] = max(arr[1],arr[0] + arr[1]) # 두 번째 계단의 인덱스 = 1
    dp[2] = max(arr[0]+arr[2],arr[1]+arr[2]) # 세 번째 계단의 인덱스 = 2
    for i in range(3,T): # i번째(즉, 도착점) 계딘의 인덱스 = i - 1 이 된다. 따라서 range가 T까지이다.
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])
    print(dp[T-1])