R,C,W = map(int,input().split())
# dp[i][j] = dp[i-1][j] + dp[i-1][j-1] 
# dp[i][0] = 1, dp[i][j] (i==j) = 1
# dp[i][j] = i C j 의 값
# dp는 0행 0열로 시작
dp =[[0 for col in range(33)] for row in range(33)]
# print(dp)
dp[0][0] = 1
for i in range(1,33):
    for j in range(33):
        if j == 0 :
            dp[i][j] = 1
        elif i == j:
            dp[i][j] = 1
        elif i < j: 
            pass
        else: dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
# print(dp[R-1][C-1]) #시작값
sum = 0
w = C-1
for i in range(R-1,R-1+W): 
    for j in range(C-1,w+1):
        sum +=dp[i][j]
    w += 1 # (2,0) /(3,0)(3,1)/(4,0)(4,1)(4,2)/(5,0)(5,1)(5,2)(5,3) 인덱스 넣어서 계산하는 방법
           # 길이가 1씩 커지므로 w라는 변수 도입해서 += 1 더해서 j의 범위를 1개씩 늘려가자
print(sum)