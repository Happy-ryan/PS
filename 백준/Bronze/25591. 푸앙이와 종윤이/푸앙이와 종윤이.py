N,M = map(int,input().split())
a = 100 - N
b = 100 - M
c = 100 - (a+b)
d = a*b
q = d//100
r = d%100

if d>= 10:
    print(a,b,c,d,q,r)
    print(c+q,r)
else:
    print(a,b,c,d,q,r)
    print(c,d)