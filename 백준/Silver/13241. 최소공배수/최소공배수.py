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
        return gcd(b,a%b) # [큰수] = [작은수1]*몫 + [나머지1]
                          # [작은수1] =[나머지1]*몫 + [나머지2]
a,b = map(int,input().split())
print(a*b//gcd(a,b))