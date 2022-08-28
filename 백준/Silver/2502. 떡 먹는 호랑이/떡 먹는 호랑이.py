D, K = map(int,input().split())
dp = ['']* 31
dp[1] = 'a'
dp[2] = 'b'

for i in range(3,31):
    dp[i] = dp[i-1] + dp[i-2]

x = dp[D].count('a') #  a의 개수
y = len(dp[D]) - x # b의 개수
# print(x,y)
# 41 = 3 * 'a' + 5 * 'b'

for a in range(1,100001):
    b = (K - x*a)//y
    if (b >= a) and ((K - x * a) % y) == 0:
        print(a)
        print(b)
        break
    