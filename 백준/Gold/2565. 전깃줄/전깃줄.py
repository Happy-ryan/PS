n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort( key = lambda x : x[0])

dp = [1] * n # 1개는 기본적으로 가능하다.
for i in range(n):
    for j in range(i): # 내 앞까지 본다.
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))