n = int(input())
nums = [list(map(int, input().split())) for _ in range(9)]

max_val = (0, 0)
for idx, num in enumerate(nums):
    max_val = max(max_val, (max(num), idx))
    
dong = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']

print(dong[max_val[1]])