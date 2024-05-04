n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 순서가 영향을 안주는 동전 유형! + 경우의 수 
# 순서가 영향을 안준다 -> 코인을 한번 쓰고 / 다른 코인을 쓰면 / 썻던 코인을 쓰면 안돼
# 111111 / 55 / 111  (x)
# 중복 사용 가능!
def solution(n, k, coins):
    # 중복사용 가능 + 경우의 수 + 순서가 상관 없는 경우
    # dp[money] += dp[money - coin]
    # 경우의 수 - 0으로 한다!
    dp = [0 for _ in range(k + 1)]
    
    dp[0] = 1
    # 코인을 중복사용은 가능하되, 쓰고나면 다음에는 쓰지 못함
    # 그래서 코인이 먼저 소비시켜야함!
    for coin in coins:
        for money in range(1, k + 1):
            if money - coin >= 0:
                dp[money] += dp[money - coin]
                
    return dp[k]

def solution_1(n, k, coins):
    # 중복사용 가능 + 경우의 수 + 순서가 다르면 다른 경우
    dp = [0 for _ in range(k + 1)]
    
    dp[0] = 1
    for money in range(1, k + 1):
        for coin in coins:
            if money - coin >= 0:
                dp[money] += dp[money - coin]
                
    return dp[k]
    

print(solution(n, k, coins))