# 선택하면 그 잔 모두 섭취
# 연속 3개 섭취 불가!
# 최대로 마실 수 있는 포도주의 양

n = int(input())
nums = [int(input()) for _ in range(n)]

def solution(n, nums):
    # dp[i][j] i번째 와인까지 봐서 j개를 연속으로 골랐을 때의 포도주의 최대량
    # '3연속'이 불가능!! 최대 연속이다!
    # dp[i][1]은 i가 0 ~ i - 2까지 값 중 최대값에 nums[i]를 더한다.
    # i - 2 와 i는 연속하지 않기때문에 dp[0 ~ (i - 2)][1~2]를 모두 관찰해야함.
    # dp[i][2]는 연속하다는 의미이므로 바로 내 앞의 dp[i - 1][1]에 nums[i]를 더한다.
    inf = int(1e9)
    dp = [[-inf for _ in range(3)] for _ in range(n + 1)]
    nums = [0] + nums
    dp[0][0] = 0

    for i in range(1, n + 1):
        dp[i][0] = max(dp[i-1])
        dp[i][1] = dp[i - 1][0] + nums[i]
        dp[i][2] = dp[i - 1][1] + nums[i]

    max_ans = 0
    for row in dp:
        max_ans = max(max_ans, max(row))
        
    return max_ans

print(solution(n, nums))