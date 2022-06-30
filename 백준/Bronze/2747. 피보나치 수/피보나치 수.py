#탑다운 다이나믹 프로그래밍 소스코드 - 피보나치수열
dp = [0]*100 #계산된 결과를 메모이제이션하기 위한 리스트 초기화
#재귀함수로 구현한 피보나치 + 탑다운
def fibo(x):
    if x == 1 or x==2:  #종료조건
        return 1
    if dp[x] != 0: #0이 아니라는 것은 이미 계산된 값이 리스트에 저장되었다는 의미
        return dp[x]
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]

N = int(input())
print(fibo(N))
