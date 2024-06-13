n = int(input())
arr = list(map(int, input().split()))
arr.append(int(-1e9))

ans = 0
s = 0
for i, x in enumerate(arr):
    if s == i or arr[i - 1] < arr[i]:
        continue
    else:
        ans = max(ans, arr[i - 1] - arr[s])
        s = i
print(ans)
