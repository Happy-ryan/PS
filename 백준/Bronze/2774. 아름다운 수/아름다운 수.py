from collections import Counter

t = int(input())
for _ in range(t):
    nums = Counter(list(input()))
    print(len(nums.keys()))
    

