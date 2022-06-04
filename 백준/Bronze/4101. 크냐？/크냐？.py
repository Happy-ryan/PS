while True:
  arr = list(map(int,input().split()))
  if arr[-1]==0:
    break
  else:
    if arr[0] > arr[-1]:
      print("Yes")
    else: print("No")