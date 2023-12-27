# https://www.acmicpc.net/problem/14476


# 시간복잡도: O(log(min(a, b)))
def gcd(a: int, b: int):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
arr = list(map(int, input().split()))
prefix_left = [0] * (n + 1)
prefix_right = [0] * (n + 1)

for idx in range(1, n + 1):
    # gcd(a, b): b가 0일 때 a 그대로 출력
    prefix_left[idx] = gcd(arr[idx - 1], prefix_left[idx - 1])

for idx in range(n, 0, -1):
    prefix_right[idx - 1] = gcd(arr[idx - 1], prefix_right[idx])


res = [0] * (n)

ans = -1
for idx, k in enumerate(arr):
    exclude_gdc = gcd(prefix_left[idx], prefix_right[idx + 1])
    if k % exclude_gdc != 0:
        ans = max(ans, exclude_gdc)
        res[idx] = ans

if max(res) == 0:
    print(-1)
else:
    print(max(res), arr[res.index(max(res))])