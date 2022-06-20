T = int(input())
for _ in range(T):
    arr = input().split()
    arr[0] = arr[0].title()
    print(*arr)