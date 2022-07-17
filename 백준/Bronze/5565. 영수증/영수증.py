arr = [int(input()) for col in range(10)]
total = arr[0]
for x in range(1,10):
  total -= arr[x]
print(total)