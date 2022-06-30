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
    arr = list(map(int,input().split()))
    result = []
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            result.append(gcd(arr[i],arr[j]))
    print(max(result))