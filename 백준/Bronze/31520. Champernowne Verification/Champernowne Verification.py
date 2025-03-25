dp = [0] * 11
dp[1] = '1'
for i in range(2, 11):
    dp[i] =  dp[i - 1] + str(i)

x = input()

try :
    ans = dp.index(x)
except:
    ans = -1
    
print(ans)