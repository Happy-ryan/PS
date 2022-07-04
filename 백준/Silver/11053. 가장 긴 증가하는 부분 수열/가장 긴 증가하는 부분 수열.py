n = int(input())
arr = list(map(int,input().split()))
# dp[i] = 인덱스 i를 반드시 선택했을 때 증가하는 부분 수열의 최대 길이
dp = [0] *1003
dp[0] = 1
for i in range(1,n):
    result = []
    for j in range(0,i):
        if arr[j] < arr[i]: # i번을 반드시 선택했을 때 arr[i]보다 작은 값들의 dp[j] 구하고 넣기
            result.append(dp[j])
            dp[i] = max(result) +1
        else:
            if dp[j] !=1:
                continue
            else: dp[i] = 1
print(max(dp))