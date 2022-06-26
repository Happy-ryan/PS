N = int(input())
arr = sorted([int(input()) for _ in range(N)])
cnt = {}
for x in arr:
    if x not in cnt:
        cnt[x] = 0
    cnt[x] += 1
ret = max(cnt.values())
brr = sorted([x[0] for x in cnt.items() if x[1] == ret])

print(round(sum(arr) / N))
print(arr[N//2])
print(brr[len(brr) > 1])
print(arr[-1] - arr[0])