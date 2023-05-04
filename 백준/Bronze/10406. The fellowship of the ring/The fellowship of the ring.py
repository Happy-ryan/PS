middle, top, t = map(int, input().split())
nums = list(map(int, input().split()))
sum_val = 0
for num in nums:
    if middle <= num and num <= top:
        sum_val += 1

print(sum_val)