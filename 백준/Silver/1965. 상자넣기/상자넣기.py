n = int(input())
arr = list(map(int,input().split()))
# 인덱스i를 선택했을 때 0~(i-1)까지의 인덱스 중에서 크기가 작은 놈을 넣을 수 있다.
dp = [1]*(n+1)
for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],1+dp[j])

print(max(dp))