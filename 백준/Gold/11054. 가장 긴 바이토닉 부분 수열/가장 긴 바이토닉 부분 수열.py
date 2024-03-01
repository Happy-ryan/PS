n = int(input())
nums = list(map(int, input().split()))
# 증가 -> 감소

def solution(n, nums):
    dp = [-1 for _ in range(n)]
    # dpf(x) = x번째에 도착했을 때 증가하는 부분수열의 최대 길이
    # dpf(x) = max(dpf(i) where 0 <= i < x) + 1
    def dpf(x, nums, dp):
        if dp[x] != -1:
            return dp[x]
        
        ret = 0
        is_start = True
        for i in range(x):
            if nums[x] > nums[i]:
                ret = max(ret, dpf(i, nums, dp) + 1)
                is_start = False

        if is_start:
            return 1

        dp[x] = ret

        return ret

    rnums = nums[::-1]
    rdp = [-1 for _ in range(n)]
    max_ans = 0
    for x in range(n):
        # print("최장 증가 수열 - 도착점의 인덱스", x, "도착점", nums[x], "최장길이", dpf(x, nums, dp))
        # print("(역방향) 최장 증가 수열 - 도착점의 인덱스", n - x - 1, "도착점", rnums[n - x - 1], "최장길이", dpf(n - x - 1, rnums, rdp))
        l = dpf(x, nums, dp)
        r = dpf(n - x - 1, rnums, rdp)
        max_ans = max(l + r - 1, max_ans)
        # print("인덱스: ", x, "l: ", l, "r: ",r)
        # print("=")

    return max_ans

print(solution(n, nums))