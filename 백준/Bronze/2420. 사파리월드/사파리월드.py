N,M = map(int, input().split())
result = N-M if N>M else M-N
print(result)