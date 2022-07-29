import math
n = int(input())
# dp[i] 숫자i를 제곱수의 합으로 나타낼 때 그 제곱수 항의 최소 개수
# 주의사항 i보다 작은 최대 제곱수+나머지를 한다고 최소 항이 되는 것 아니다.
# 18 = 16+1+1, 9+9 알 수 있듯이 최소항은 다를 수 있다는 점을 주의하자.

dp = [0] * (n+1)
dp[1] = 1

for i in range(2,n+1):  
    result_set =set()
    for j in range(1,int(math.sqrt(i))+1):
        dp[i] = 1+dp[i-j**2]
        result_set.add(dp[i])
    dp[i] = min(result_set)

print(dp[n])