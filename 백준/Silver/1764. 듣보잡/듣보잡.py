N,M = map(int, input().split())
arr = [ input() for _ in range(N)]
brr = set(input() for _ in range(M))
result=[]
for x in arr:
    if x in brr:
        result.append(x)
print(len(result))
print(*sorted(result), sep="\n")