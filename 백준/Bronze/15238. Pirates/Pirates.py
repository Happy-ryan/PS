from collections import Counter
n = int(input())
arr = Counter(list(input()))
max_value = max(arr.values())
for key, value in arr.items():
    if value == max_value:
        print(key, value)
        break