n = int(input())
arr = [list(map(int,input().split())) for row in range(n)] 
# print(arr)

# dp[i] row (0~n-1) = i층까지의 최대의 합 
# j col(0~len(row)-1) = i층에서 최대 합이 되게 하는 
# 이 문제의 포인트는 n-2층까지의 누적합이 최소여도 마지막 층에서 엄청 큰 수가 더해지면 최대합이 바뀔 수 있다. 
# 따라서 트리모양처럼 각 층의 호수에 누적합을 더해줘서 (n-1)층에서의 최대합을 찾는다.
dp = [[ 0 for col in range(n) ] for row in range(n)] #2차원 배열 dp 초기화
# print(dp)
dp[0][0] = arr[0][0] # i=0이 제일 윗층
# print(dp)
for i in range(1,n):
    for j in range(0,len(arr[i])):
        if j ==0 : # 1호(j=1~n-2)와 층의 마지막 호는 선택받을 수가 없다. 그 전 층의 호수의 최대합 가져와야한다.
            dp[i][j] = dp[i-1][j] + arr[i][j] 
        elif j == len(arr[i])-1:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else: # j = 1~ : 내가 j = 1이면 j = 0 과 j = 1에서 값을 가져올 수 있다.
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + arr[i][j]

print(max(dp[n-1]))