n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

def solution(n, nums):
    memo = [0,0,0]
    
    for i in range(n):
        for j in range(3):
            memo[j] += nums[i][j]

        if memo[0] < 30 or memo[1] < 30 or memo[2] < 30:
            print("NO")
        else:
            d = min(memo)
            print(d)
            memo[0] -= d
            memo[1] -= d
            memo[2] -= d
            

solution(n, nums)