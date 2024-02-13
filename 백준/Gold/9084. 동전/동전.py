t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    
    dp = [1] + [0 for _ in range(money)]
    
    for x in coins:
        for i in range(x, money + 1):
            dp[i] += dp[i - x]
            
    print(dp[money])