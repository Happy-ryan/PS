# https://www.acmicpc.net/problem/1182
# 시간복잡도
# -> 20C1+20C2+...20C19 2^20 = 1000 1000 = 1000000(백만)
from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for x in range(1, n + 1):
    for row in combinations(arr, x):
        if sum(row) == s:
            cnt += 1

print(cnt)