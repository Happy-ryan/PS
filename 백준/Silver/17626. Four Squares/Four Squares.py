n = int(input())
# dp[i] : 숫자i를 제곱수로 표현하는 최소 방법의 수
arr = [i**2 for i in range(1,224)]
dp = [5]*50001

for i in range(1,224):
    dp[i**2] = 1

for x in range(2,n+1):
    for i in arr:
      if i <= x:
          dp[x] = min(dp[x],dp[x-i]+1)

print(dp[n])