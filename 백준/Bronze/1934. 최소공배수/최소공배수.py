def gcd(a,b):
    if a < b:
        small = a
        a = b
        b = small
    else: 
        pass # a > b 상태로 만들기
    
    if a%b == 0 :
        return b
    else:
        return gcd(b,a%b)

T = int(input())
for row in range(T):
    a,b = map(int,input().split())
    print(a*b//gcd(a,b))