from collections import Counter

nums = [int(input()) for _ in range(5)]

dic = Counter(nums)

for x, y in list(dic.items()):
     if (y % 2 != 0):
        print(x)
        break
