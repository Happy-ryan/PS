n = int(input())
for x in reversed(range(n)):
    print(" "*(n-1-x)+"*"*(2*x+1))
for y in range(2,n+1):
    print(" "*(n-y)+"*"*(2*y-1))