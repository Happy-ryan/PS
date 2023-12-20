n = int(input())
nums = list(map(int, input().split()))
nums.sort()

# target보다 작거나 같은 값 중 가장 큰 값
def binary_search(idx: int):
    target = -nums[idx]
    l, r = idx + 1, n - 1
    ans = l
    while l <= r:
        m = (l + r) // 2
        if nums[m] <= target:
            l = m + 1
            ans = m
        else:
            r = m - 1
    return ans

# target보다 크거나 같은 값 중 가장 작은 값
def binary_search1(idx: int):
    target = -nums[idx]
    l, r = idx + 1, n - 1
    ans = l
    while l <= r:
        m = (l + r) // 2
        if nums[m] >= target:
            r = m - 1
            ans = m
        else:
            l =  m + 1
    return ans

def solve(isTrue):
    pair = 0
    inf = 1000000000
    ans = inf * 2 + 1
    for idx in range(n - 1):
        if isTrue:
            k = binary_search1(idx)
        else:
            k = binary_search(idx)
        sum_val = abs(nums[idx] + nums[k])
        if sum_val <= ans:
            ans = sum_val
            pair = (nums[idx], nums[k])
            
    return pair

if abs(sum(solve(True))) > abs(sum(solve(False))):
    print(*solve(False))
else:
    print(*solve(True))