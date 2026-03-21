from collections import Counter

n = int(input())
nums = Counter(list(map(int, input().split())))

for key, value in nums.items():
    if value == 1:
        print(key)
        break