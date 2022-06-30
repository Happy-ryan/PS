n,m = map(int,input().split())
dp = [[0 for col in range(33)] for row in range(33)]

def C(x,y):
    if y == 0 :
        return 1
    elif x == y :
        return 1
    else:
        if dp[x][y] != 0:
            return dp[x][y]
        else:
            dp[x][y] = C(x-1,y-1)+C(x-1,y)
            return dp[x][y]

print(C(n-1,m-1))