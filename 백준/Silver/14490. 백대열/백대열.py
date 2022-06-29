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

a,b = map(int,input().split(':'))
gcd_num = gcd(a,b)
# print(gcd_num)
# print(a//gcd_num)
# print(b//gcd_num)
print('%d:%d' %(a//gcd_num,b//gcd_num))