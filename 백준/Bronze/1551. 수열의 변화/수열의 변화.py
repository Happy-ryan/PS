N, K = map(int,input().split())
arr = list(map(int, input().split(',')))
cnt = 0
if K == 0:
  result =','.join(map(str,arr))
  print(result)
else:
  while cnt != K:
    brr = []
    for i in range(len(arr)-1): # 길이가 반복문을 돌 때마다 -1씩 줄어든다. 범위를 N으로 하면 안된다.
      brr.append(arr[i+1]-arr[i]) 
    cnt += 1
    arr = brr
  # print(brr)
  result = ','.join(map(str,brr))
  print(result)