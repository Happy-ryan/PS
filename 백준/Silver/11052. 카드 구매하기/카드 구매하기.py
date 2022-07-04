n = int(input())
prices = list(map(int,input().split()))
#dp[i] i개의 카드를 구매할 때 금액의 최대값
dp = [0] * 1003
dp[1] = prices[0] 
dp[2] = max(dp[1]*2,prices[1])
for i in range(3,n+1):
    for j in range(1,i):
        dp[i] = max(dp[i],prices[j-1]+dp[i-j],prices[j]) #dp[i] 넣은 이유는 max로 갱신하기 위해서
        #pricese[j]은 즉 카드팩 1개를 샀을 때의 경우도 고려하는 것.
print(max(dp))