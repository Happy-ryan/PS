t = int(input())
for _ in range(t):
    arr = list(input().split())
    res = arr[2:] + arr[:2]
    print(*res)