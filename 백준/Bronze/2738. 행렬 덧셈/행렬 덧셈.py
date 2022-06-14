N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
brr = [list(map(int,input().split())) for _ in range(N)]
# list(mpa())
result = [[ 0 for _ in range(M)] for _ in range(N)] #리스트컴프리헨션
# print(arr)
# print(brr)
# print(result)
for i in range(N):
  for j in range(M):
    result[i][j] = arr[i][j] + brr[i][j]
for row in result:
  print(*row)