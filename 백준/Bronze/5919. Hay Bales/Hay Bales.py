n = int(input())
nums = [int(input()) for _ in range(n)]

height = sum(nums) // n
val = 0
for num in nums:
    if num > height:
        val += abs(num - height)
print(val)