n = int(input())
arr = list(map(int,input().split()))
# dp[i] 인덱스i 요소를 반드시 선택했을 때 0~i-1까지 감소하는 부분 수열의 길이
# 연속일 필요는 없다!! 
# 인덱스i를 반드시 선택했을 때 앞에 arr[i]보다 큰 수가 가지는 dp를 판단하면 된다.
dp = [1]*(n+1)
for i in range(1,n):
    dp_list =[]
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i],1+dp[j])
# print(dp)
print(max(dp))