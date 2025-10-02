nums = list(map(int, input().split()))
A, L = map(int, input().split())

tk = sum(nums[i] * nums[i+1] for i in range(0, 10, 2)) // 5

print((A * tk) // L)