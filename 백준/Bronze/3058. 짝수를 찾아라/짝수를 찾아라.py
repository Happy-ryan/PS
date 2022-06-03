T = int(input())
for _ in range(T):
  arr2 = []
  arr = list(map(int, input().split()))
  for x in arr:
    if x%2==0:
      arr2.append(x)
      arr2 = sorted(arr2)[::-1]
  print(sum(arr2),arr2[-1])