n = int(input())
nums = list(map(int, input().split()))

min_num = min(nums)

print(nums.index(min_num))