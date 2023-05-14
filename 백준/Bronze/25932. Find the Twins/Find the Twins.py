# https://www.acmicpc.net/problem/25932

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    print(*arr)
    if 17 in arr and 18 in arr:
        print("both")
    elif 17 in arr and 18 not in arr:
        print("zack")
    elif 17 not in arr and 18 in arr:
        print("mack")
    else:
        print("none")
    print()