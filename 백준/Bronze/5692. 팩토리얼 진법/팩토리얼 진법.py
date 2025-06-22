def solution(num):
    dp = [0] * 10
    
    dp[0] = 1
    for i in range(1, 10):
        dp[i] = i * dp[i - 1]
    
    # print(dp)
    
    val = 0
    for idx, x in enumerate(str(num)):
        val += dp[len(str(num)) - idx] * int(x)
        # print(val)
    
    return val

while True:
    num = int(input())
    if num == 0:
        break
    print(solution(num))