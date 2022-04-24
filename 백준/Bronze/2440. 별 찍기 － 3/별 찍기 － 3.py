N = int(input())
print(*["*"*(N-i) for i in range(N)], sep="\n")