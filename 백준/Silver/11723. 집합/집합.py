import sys
M = int(sys.stdin.readline())
S = set()
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for _ in range(M):  
  arr = sys.stdin.readline().split()
  if arr[0]=='add': # set운 중복제거기때문에 존재할 때는 추가해도 아무 이상 없으므로 없을 때만 체크하면된다.
    if int(arr[1]) not in S:
      S.add(int(arr[1]))
  elif arr[0] =='remove': # remove요소 없으면 에러니까 만드니 pass필요
    S.discard(int(arr[1])) # discard는 요소 없어도 에러 안뜬다
  elif arr[0]=='check':
    if int(arr[1]) in S:
      print(1)
    else: print(0)
  elif arr[0]=='toggle':
    if int(arr[1]) in S:
      S.discard(int(arr[1]))
    else: S.add(int(arr[1]))
  elif arr[0]=='all':
    S.clear()
    S.update(a)
  else: 
    S.clear()