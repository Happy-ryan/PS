n = int(input())
arr = ''
for x in range(1, n + 1):
    arr += str(x)

print(arr.find(str(n)) + 1)