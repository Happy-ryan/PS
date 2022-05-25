N = int(input())
arr = [map(int,input().split()) for _ in range(N)] # list comprehension
for i in range(N):
    brr = sorted(arr[i])
    print(brr[-3])