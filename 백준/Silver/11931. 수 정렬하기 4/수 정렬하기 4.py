N = int(input())
arr=[]
for x in range(N):
    n = int(input())
    arr.append(n)
arr = sorted(arr)
for x in reversed(arr):
    print(x)