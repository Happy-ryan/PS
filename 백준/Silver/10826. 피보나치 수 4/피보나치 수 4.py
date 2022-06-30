n = int(input())
dp = [0]*10004 #계산된 결과를 메모이제이션하기 위한 리스트 초기화
#재귀문으로 했을 경우 RecursionError 발생 > 재귀문 없이 반복문으로 DP하기
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])