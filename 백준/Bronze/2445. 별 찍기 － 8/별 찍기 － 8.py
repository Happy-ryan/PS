n = int(input())
for x in range(1,n+1):
    print("*"*x+" "*(2*n-2*x)+"*"*x)
for x in reversed(range(1,n)):
    print("*"*x+" "*(2*n-2*x)+"*"*x)