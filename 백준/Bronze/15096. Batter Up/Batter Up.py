n = int(input())
nums = list(map(int, input().split()))

sum_val, cnt = 0, n
for x in nums:
    if x >= 0:
        sum_val += x
    else:
        cnt -= 1
        
print(sum_val / cnt)