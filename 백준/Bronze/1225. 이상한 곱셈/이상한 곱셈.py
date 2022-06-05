A, B = input().split()
sum = 0
for x in A :
  for y in B:
    sum += int(x) * int(y)
print(sum)   