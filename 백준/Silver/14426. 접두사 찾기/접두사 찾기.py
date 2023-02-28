def getPrefix(arr):
    prefix = set()
    for row in arr:
        for i in range(1, len(row) + 1):
            prefix.add(row[0 : i])
    return prefix

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
brr = [input() for _ in range(m)]
pre = getPrefix(arr)

cnt = 0
for x in brr:
    if x in pre:
        cnt += 1
        
print(cnt)