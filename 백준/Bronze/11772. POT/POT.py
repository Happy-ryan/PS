n = int(input())
nums = [int(input()) for _ in range(n)]

sum_val = 0

for num in nums:
    sum_val += (num // 10) ** (num % 10)

print(sum_val)