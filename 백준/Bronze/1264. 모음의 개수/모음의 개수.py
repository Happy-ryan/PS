brr = ['a','e','i','o','u','A','E','I','O','U']
while True :
  arr = input()
  if '#' in arr:
    break
  else:
    cnt = 0
    for x in arr:
      if x in brr:
        cnt +=1
    print(cnt)