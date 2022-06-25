arr = [input() for row in range(28)]
arr = sorted([int(a) for a in arr])
# print(arr)
for x in range(1,31):
    if x in arr:
        continue
    else: print(x)