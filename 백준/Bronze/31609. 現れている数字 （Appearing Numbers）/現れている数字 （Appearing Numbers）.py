n = int(input())
arr = sorted(list(set(list(map(int, input().split())))))
for x in arr:
    print(x)