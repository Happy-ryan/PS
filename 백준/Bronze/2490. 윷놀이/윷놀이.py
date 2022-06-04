arr = [ input().split() for _ in range(3)]
arr=[[int(a),int(b),int(c),int(d)] for a,b,c,d in arr]
for i in range(3):
  if sum(arr[i]) == 3:
    print("A")
  elif sum(arr[i]) == 2:
    print('B')
  elif sum(arr[i])==1:
    print('C')
  elif sum(arr[i])==4:
    print('E')  
  else: print('D')