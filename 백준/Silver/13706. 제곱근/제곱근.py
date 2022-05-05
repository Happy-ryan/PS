N = int(input())

l,r = 1, 10**400    # l과r은 제곱근을 의미하는 것들 : 1,2,3,4....10**400
while r-l != 1:    # 찾아야 하는 것 : N의 제곱근을 찾는 것 BY 이분탐색
    m =(r+l)//2     # m도 제곱근을 의미한다. 
    if m*m < N:
        l = m
    else: r= m

print(r)