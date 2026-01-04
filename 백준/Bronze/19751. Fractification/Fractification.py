a, b, c, d = map(int, input().split())

# 정렬
nums = sorted([a, b, c, d])

# 최적 배치: x1/x3 + x2/x4
print(nums[0], nums[2], nums[1], nums[3])