N = int(input())
arr = [input() for _ in range(N)]
arr = list(set(arr))
arr = sorted([(len(s), s) for s in arr])
arr = [x[1] for x in arr]
print(*arr, sep='\n')