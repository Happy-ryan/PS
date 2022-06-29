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
n = int(input())
arr = list(map(int,input().split()))
for i in range(1,n):
    gcd_num = gcd(arr[0],arr[i])
    print('%d/%d' %(arr[0]//gcd_num,arr[i]//gcd_num ))