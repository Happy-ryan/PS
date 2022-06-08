N = int(input())
F = int(input())
arr = list(str(N))
result = set()
for x in range(0,10):
  for y in range(0,10):
    arr[-1], arr[-2]= x, y
    M = 0
    for i in range(len(arr)):
     M += int(arr[i])*10**(len(arr)-i-1)
    if M % F ==0:
      result.add(M)
# print(min(result))
ans = list(str(min(result)))
# print(ans)
print(ans[-2]+ans[-1])