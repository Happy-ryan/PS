N, X = map(int, input().split())
arr = list(map(int, input().split()))
for j in arr :
    if j < X :
        print(j, end=" ")