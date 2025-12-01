from collections import Counter

n = int(input())
arr = Counter([int(input()) for _ in range(n)])
max_cnt = 0
for val in arr.values():
    max_cnt = max(max_cnt, val)
    
print(max_cnt)