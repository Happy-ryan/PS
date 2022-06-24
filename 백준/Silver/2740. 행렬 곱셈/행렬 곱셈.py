n,m = map(int,input().split()) # n 행 m 열
arr = [list(map(int,input().split())) for _ in range(n)]
# print(arr)
# print(arr[0])
# print(arr[0][1])
m,k = map(int,input().split()) # m 행 n 열
brr = [list(map(int, input().split())) for _ in range(m)]
# print(brr)
# print(brr[0])
result =[[ 0 for _ in range(k)] for _ in range(n) ]
# print(result)
for i in range(n):
    for z in range(k):
        for j in range(m):
            result[i][z] += arr[i][j]*brr[j][z]
# print(result)
for i in range(n):
    print(*result[i])