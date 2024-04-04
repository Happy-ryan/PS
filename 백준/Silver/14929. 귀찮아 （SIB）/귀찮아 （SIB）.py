n = int(input())
nums = list(map(int, input().split()))


def solution(n, nums):
    # x1 (x2 + x3) + x2(x3)
    psum = [0] * n
    for i in range(n - 2, -1, -1):
        psum[i] = psum[i + 1] + nums[i + 1]

    ans = 0
    for i in range(n):
        ans += nums[i] * psum[i]

    return ans


print(solution(n, nums))
