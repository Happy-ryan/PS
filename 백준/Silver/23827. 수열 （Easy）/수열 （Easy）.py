n = int(input())
nums = list(map(int, input().split()))


def solution(n, nums):
    # 모든 쌍의 개수이므로 순서는 무관함.
    nums.sort()
    mod = 1000000007
    # x1 x2 x3 x4
    # x1 * x2 + x1 * x3 + x1 * x4
    # x2 * x3 + x2 * x4
    # x3 * x4
    # = x1 (x2 + x3 + x4) + x2 (x3 + x4) + x3 (x4)
    # 인덱스 x 의 숫자 * (인덱스 x + 1 ~ 끝까지의 누적합)
    # 반드시 끝이 들어가므로 반대방향 누적합을 하는게 적절해보인다.
    # psum[i]의 정의
    # 1 2 3
    # 5 3 0
    # psum[1] = psum[2] + nums[2]
    # psum[0] = psum[1] + nums[1]
    psum = [0] * n
    for i in range(n - 2, -1, -1):
        psum[i] = psum[i + 1] + nums[i + 1]

    ans = 0
    for i in range(n):
        ans += (nums[i] * psum[i]) % mod

    return ans % mod


print(solution(n, nums))