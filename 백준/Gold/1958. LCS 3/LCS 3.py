X = input()
Y = input()
Z = input()
def LCS(X, Y, Z):
    X = '0' + X
    Y = '0' + Y
    Z = '0' + Z
    dp = [ [[0 for j in range(len(Y))] for i in range(len(X))] for d in range(len(Z)) ]
    ans = 0
    for d in range(1, len(Z)):
        for i in range(1, len(X)):
            for j in range(1, len(Y)):
                if X[i] == Y[j] == Z[d]:
                    dp[d][i][j] = dp[d-1][i-1][j-1] + 1
                else:
                    dp[d][i][j] = max( dp[d-1][i][j], dp[d][i-1][j], dp[d][i][j-1],\
                                    dp[d-1][i-1][j], dp[d-1][i][j-1], dp[d][i-1][j-1] )
            ans = max(ans, dp[d][i][j])
    
    return ans

print(LCS(X, Y, Z))