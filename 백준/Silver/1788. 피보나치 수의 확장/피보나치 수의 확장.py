n = int(input())

dp_plus = [0] *1000006
dp_minus = [0]*1000006
mod = 1000000000
if n==0:
    print(0)
    print(0)
elif n >0:
    dp_plus[0] = 0
    dp_plus[1] = 1
    for i in range(2,n+1):
        dp_plus[i] = (dp_plus[i-1]+dp_plus[i-2])%mod
    print(1)
    print(dp_plus[n])
else:
    dp_minus[0] = 0 #dp[0]
    dp_minus[1] = 1 #dp[-1]의미
    dp_minus[2] = -1 #dp[-2]의미
    for i in range(3,(-n)+1):
        dp_minus[i] = dp_minus[i-2] - dp_minus[i-1]
        if dp_minus[i] > 0:
            dp_minus[i] = (dp_minus[i])%mod
        else: #((-정수 %  mod ) 하면 원하는 나머지가 나오지 않으므로 양수로 바꾸고 나서 -부호 붙이는 방법을 사용한다.
            dp_minus[i] = -(abs(dp_minus[i])%mod)
    if dp_minus[-n] > 0:
        print(1)
        print(abs(dp_minus[-n]))
    else: 
        print(-1)
        print(abs(dp_minus[-n]))
