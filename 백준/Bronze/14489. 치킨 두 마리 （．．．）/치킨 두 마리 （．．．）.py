a,b = map(int, input().split())
price = int(input())

if a+b < 2*price :
    print(a+b)
else :
    print(a+b-(2*price))