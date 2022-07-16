n = int(input())
for x in reversed(range(1,n+1)):
    print(' '*(n-x) +'*'*(2*x-1))