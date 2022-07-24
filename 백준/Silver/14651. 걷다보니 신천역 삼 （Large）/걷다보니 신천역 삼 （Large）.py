n = int(input())
dp = [[0 for col in range(3)] for row in range(n+1)]
mod = 1000000009
# dp[i][j] = i는 자릿수 // j는 3으로 나눈 나머지들(0,1,2)
# dp[i][0] 에 어떤 수가 있는지는 궁금한게 아니다.
# 어떤 수 x가 있을 때 뒤에 0을 붙이면 3의배수
# 어떤 수 x가 있을 때 뒤에 1을 붙이면 dp[i+1][1]로 이동
# 어떤 수 x가 있을 때 뒤에 2를 붙이면 dp[i+1][2]로 이동
# 즉 경우의 수로 문제를 풀 수 있는 이유(어떤 숫자인지 중요x)는 각 수를 붙였을 때 이동하는 열이 명확하기 때문
# j = 2 인 상태에서 1을 붙이면 0열로 2를 붙이면 1열로 0을 붙이면 2열로 그 j의 상태를 가지고 경우의 수가 이동
dp[1][1] = 1
dp[1][2] = 1
for i in range(2,n+1):
    for j in range(3):
        for add in range(3):
            dp[i][(j+add)%3] += dp[i-1][j]
            dp[i][(j+add)%3] = dp[i][(j+add)%3]%mod
print(dp[n][0]%mod)