N = int(input())
M = int(input())
arr = [int(input()) for col in range(M)]
# print(arr)
# dp[i] 자리가 i개 일때 바꿀 수 있는 경우의 수
dp = [0] *(41)
dp[1] = 1
dp[2] = 2
for i in range(3,N+1):
    dp[i] = dp[i-1]+dp[i-2]
# print(dp)
if M==0:
    print(dp[N])
else:
    check = arr.copy()
    result = []
    for i in range(M-1):
        result.append(check[i+1]-check[i]-1)
    result.append(check[0]-1)
    result.append(N-check[-1])

    sum = 1
    for x in result:
        if x > 0:
            sum *= dp[x]

    print(sum)