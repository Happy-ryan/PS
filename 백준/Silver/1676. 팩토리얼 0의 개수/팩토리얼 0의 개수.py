n = int(input())
s = ''
dp = [0]*(n+1)
dp[0] = 1
for i in range(1,n+1):
    dp[i] = i*dp[i-1]

for x in dp:
    s += str(x)

s = s[::-1]
# print(s)

if s[0] != '0':
    print(0)
else:
    cnt = 1
    for x in s[1:]:
        if x  == '0':
            cnt += 1
        else:
            break
    print(cnt)
        