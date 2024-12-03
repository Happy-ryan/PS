n = int(input())
nums = list(map(int, input().split()))

sum_val = 0
state = 0
for num in nums:
    if num == 1:
        state += 1
    else:
        state -= 1
    sum_val += state
    
print(sum_val)