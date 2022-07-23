n = int(input())
L = list(map(int,input().split()))
J = list(map(int,input().split()))
# 냅색 문제 행 : 가치의 수 // 열 : 한계(무게, 체력 등)
# 냅색 느낌: 내가 골드바를 넣었을 때 안넣었을 때를 보는데
# 그 이전에 넣은 것과 겹친는 곳이 존재하면 큰거(또는 작은거)로 대체한다.
dp = [[ -1 for col in range(101)] for row in range(len(J)+1)]
# print(dp) # 체력의 한계는 99다.
dp[0][0] = 0
for i in range(1,n+1):
    dp[i] = dp[i-1].copy() # 그 전에 넣었던 것의 가치를 그대로 우선 가져오기
                           # 왜냐하면 내가 이번에 넣어도 겹치지 않는 것은 그대로 가치를 가져오니까
    for j in range(100):
        if dp[i-1][j] >= 0 and j+L[i-1] < 100: # dp[i-1][j] 2가지로 나뉠 때 -1이 아니라 0이상인 상태에서 두갈래로 나뉜다. 따라서 전 상태 파악해야함
            # 체력의 한계가 100이므로 최대 99까지 더해질 수 있도록 j+L[i-1]을 체크
            dp[i][j+L[i-1]] = max(dp[i][j+L[i-1]],dp[i-1][j] + J[i-1]) # 카피를 했어도 그 전에서 가져와야 중복 발생x

print(max(dp[n]))