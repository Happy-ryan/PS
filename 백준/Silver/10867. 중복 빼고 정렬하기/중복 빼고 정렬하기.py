N = int(input())
arr = list(map(int, input().split()))
# print(set(sorted(arr)))
for x in set(sorted(arr)):
    print(x,end=" ")