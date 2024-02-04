from collections import defaultdict

n = int(input())
numbers = list(map(int, input().split()))
sorted_unique_numbers = sorted(set(numbers))

dic = defaultdict()
# NlogN
for idx, num in enumerate(sorted_unique_numbers):
    dic[num] = idx
    
for num in numbers:
    print(dic[num], end = " ")