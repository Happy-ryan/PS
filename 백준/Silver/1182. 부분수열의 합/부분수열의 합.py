#시간복잡도
# n*(nC1 + nC2 + ... nCn) = n * 2^n = 20 * 1000 * 1000

n, s = map(int, input().split())
nums = list(map(int, input().split()))


from itertools import combinations

cnt = 0
for x in range(1, n + 1):
    for row in combinations(nums, x):
        if sum(row) == s:
            cnt += 1

print(cnt)