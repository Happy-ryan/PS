n = int(input())
nums = list(map(int, input().split()))

from collections import Counter


def solution(n, nums):
    inf = int(1e18)
    # 정렬하면 안된다.
    r = 0
    # 과일의 종류
    fruits = Counter()
    ans = -inf
    for l in range(n):
        while r < n and len(fruits) < 3:
            fruits[nums[r]] += 1
            r += 1
            
        if len(fruits) == 3:
            # print(f"l: {l}, r: {r - 2}, fruit: {fruits}")
            ans = max(ans, r - 2 - l + 1)

        if len(fruits) <= 2:
            # print(f"l: {l}, r: {r - 1}, fruits: {fruits}")
            ans = max(ans, r - 1 - l + 1)

        if fruits[nums[l]] - 1 == 0:
            fruits.pop(nums[l])
        else:
            fruits[nums[l]] -= 1
            
    return ans


print(solution(n, nums))