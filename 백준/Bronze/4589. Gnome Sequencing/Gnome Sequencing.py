n = int(input())
result = []
arr = [input().split() for _ in range(n)]
for i in range(n):
  if arr[i] == sorted(arr[i]):
    result.append('Ordered')
  elif sorted(arr[i])[::-1] == arr[i]:
    result.append('Ordered')
  else:
    result.append('Unordered')

print('Gnomes:')
for row in result:
  print(row)