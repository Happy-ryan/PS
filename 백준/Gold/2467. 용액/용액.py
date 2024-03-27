n = int(input())
nums = list(map(int, input().split()))


def solution(n, nums):
    inf = int(1e18)
    # 정렬해도 상관없는 문제
    nums.sort()
    # 음수 중 최대값을 만들고 싶다!!
    # 둘의 합이 양수면 음수가 될 때까지 줄여야함(r -= 1)
    # l 고정 / r 이동
    r = n - 1
    answer_1 = -inf
    ans1 = (-inf, 0, 0)
    for l in range(n):
        while l < r and nums[l] + nums[r] > 0:
            r -= 1

        if l < r and nums[l] + nums[r] <= 0:
            answer_1 = nums[l] + nums[r]
            ans1 = max((answer_1, nums[l], nums[r]), ans1)
    # 양수 중 최소값을 만들고 싶다.
    # 둘의 합이 음수면 양수가 될 때까지 늘려야함.(l += 1)
    # l 이동 / r 고정
    l = 0
    answer_2 = inf
    ans2 = (inf, 0, 0)
    for r in range(n - 1, 0, -1):
        while l < r and nums[l] + nums[r] < 0:
            l += 1

        if l < r and nums[l] + nums[r] >= 0:
            answer_2 = nums[l] + nums[r]
            ans2 = min((answer_2, nums[l], nums[r]), ans2)

    a = ans1
    b = ans2

    if abs(a[0]) > abs(b[0]):
        return f"{b[1]} {b[2]}"
    else:
        return f"{a[1]} {a[2]}"

print(solution(n, nums))