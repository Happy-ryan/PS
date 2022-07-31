n,m = map(int,input().split())
arr = [[input()] for row in range(n)]
# print(arr)
for row in arr:
    result = row[0][::-1]
    print(result)
